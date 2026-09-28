<?php
// POST { nome, email, ... } vindo de /cadastro/: grava em `cadastros` e cria o cliente no Asaas.
require __DIR__ . '/lib.php';

cors(['POST']);
if ($_SERVER['REQUEST_METHOD'] !== 'POST') responder(['error' => 'Método não permitido'], 405);

$body = corpo_json();
$cadastro = [];
foreach (CAMPOS as $campo) {
    $v = is_string($body[$campo] ?? null) ? trim($body[$campo]) : '';
    if ($v === '' || mb_strlen($v) > 2000) responder(['error' => "Campo inválido: $campo"], 400);
    $cadastro[$campo] = $v;
}

try {
    $colunas = implode(', ', CAMPOS);
    $marcadores = implode(', ', array_fill(0, count(CAMPOS), '?'));
    db()->prepare("INSERT INTO cadastros ($colunas) VALUES ($marcadores)")->execute(array_values($cadastro));
    $cadastro['id'] = (int) db()->lastInsertId();
} catch (Throwable $e) {
    error_log('cadastro: ' . $e->getMessage());
    responder(['error' => 'Falha ao salvar o cadastro'], 500);
}

// O cadastro já está salvo; se o Asaas falhar, fica como "erro" para tentar de novo no admin.
responder(['id' => $cadastro['id']] + processar($cadastro));
