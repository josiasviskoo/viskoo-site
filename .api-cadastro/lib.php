<?php
// Funções compartilhadas por cadastro.php e admin.php.

const CAMPOS = [
    'nome', 'email', 'whatsapp', 'empresa', 'documento', 'rua', 'numero', 'bairro',
    'cep', 'cidade', 'dia_pagamento', 'descricao', 'valor', 'parcelamento',
];

$config = require __DIR__ . '/config.php';

function responder($body, int $status = 200): void
{
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

function cors(array $metodos): void
{
    global $config;
    $origem = $_SERVER['HTTP_ORIGIN'] ?? '';
    if (in_array($origem, $config['origens'], true)) {
        header("Access-Control-Allow-Origin: $origem");
        header('Vary: Origin');
        header('Access-Control-Allow-Headers: Content-Type, Authorization');
        header('Access-Control-Allow-Methods: ' . implode(', ', $metodos) . ', OPTIONS');
    }
    if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
        http_response_code(204);
        exit;
    }
}

function corpo_json(): array
{
    $body = json_decode(file_get_contents('php://input'), true);
    if (!is_array($body)) responder(['error' => 'JSON inválido'], 400);
    return $body;
}

function db(): PDO
{
    global $config;
    static $pdo;
    return $pdo ??= new PDO(
        "mysql:host={$config['db_host']};dbname={$config['db_name']};charset=utf8mb4",
        $config['db_user'],
        $config['db_pass'],
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC],
    );
}

function so_digitos(string $s): string
{
    return preg_replace('/\D/', '', $s);
}

function asaas(string $metodo, string $path, ?array $body = null): array
{
    global $config;
    $ch = curl_init($config['asaas_base_url'] . $path);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST  => $metodo,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 20,
        CURLOPT_HTTPHEADER     => [
            'Content-Type: application/json',
            'User-Agent: viskoo-site',
            'access_token: ' . $config['asaas_api_key'],
        ],
        CURLOPT_POSTFIELDS => $body === null ? null : json_encode($body, JSON_UNESCAPED_UNICODE),
    ]);
    $resposta = curl_exec($ch);
    if ($resposta === false) throw new RuntimeException('Falha de conexão com o Asaas: ' . curl_error($ch));
    $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    $json = json_decode($resposta, true) ?: [];
    if ($status >= 400) {
        $msg = implode('; ', array_column($json['errors'] ?? [], 'description'));
        throw new RuntimeException($msg ?: "Asaas respondeu $status");
    }
    return $json;
}

// Reaproveita o cliente se o CPF/CNPJ já existir no Asaas, senão cria.
function sincronizar(array $c): string
{
    $cpfCnpj = so_digitos($c['documento']);
    $existente = asaas('GET', '/customers?cpfCnpj=' . $cpfCnpj);
    if (!empty($existente['data'])) return $existente['data'][0]['id'];

    $novo = asaas('POST', '/customers', [
        'name'              => $c['nome'],
        'company'           => $c['empresa'],
        'cpfCnpj'           => $cpfCnpj,
        'email'             => $c['email'],
        'mobilePhone'       => so_digitos($c['whatsapp']),
        'address'           => $c['rua'],
        'addressNumber'     => $c['numero'],
        'province'          => $c['bairro'],
        'postalCode'        => so_digitos($c['cep']),
        'externalReference' => (string) $c['id'],
        'observations'      => "{$c['descricao']}\nValor: {$c['valor']} — {$c['parcelamento']} — dia {$c['dia_pagamento']}",
    ]);
    return $novo['id'];
}

function processar(array $c): array
{
    try {
        $asaasId = sincronizar($c);
        db()->prepare("UPDATE cadastros SET status = 'sincronizado', asaas_id = ?, erro = NULL, sincronizado_em = NOW() WHERE id = ?")
            ->execute([$asaasId, $c['id']]);
        return ['status' => 'sincronizado', 'asaas_id' => $asaasId];
    } catch (Throwable $e) {
        db()->prepare("UPDATE cadastros SET status = 'erro', erro = ? WHERE id = ?")
            ->execute([$e->getMessage(), $c['id']]);
        return ['status' => 'erro', 'erro' => $e->getMessage()];
    }
}

// ---------- Token do admin: base64url(payload).hmac ----------

function b64url(string $s): string
{
    return rtrim(strtr(base64_encode($s), '+/', '-_'), '=');
}

function gerar_token(): string
{
    global $config;
    $payload = b64url(json_encode(['exp' => time() + 12 * 3600]));
    return $payload . '.' . hash_hmac('sha256', $payload, $config['token_secret']);
}

function exigir_admin(): void
{
    global $config;
    $token = preg_replace('/^Bearer\s+/', '', $_SERVER['HTTP_AUTHORIZATION'] ?? '');
    [$payload, $assinatura] = array_pad(explode('.', $token, 2), 2, '');
    $ok = $payload !== ''
        && hash_equals(hash_hmac('sha256', $payload, $config['token_secret']), $assinatura)
        && (json_decode(base64_decode(strtr($payload, '-_', '+/')), true)['exp'] ?? 0) > time();
    if (!$ok) responder(['error' => 'Não autorizado'], 401);
}
