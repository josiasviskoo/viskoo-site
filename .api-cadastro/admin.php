<?php
// API do /cadastro/admin/:
//   POST { acao: "login", email, senha } → { token }
//   GET  (Bearer)                         → lista de cadastros
//   POST { acao: "retry", id } (Bearer)   → tenta sincronizar com o Asaas de novo
require __DIR__ . '/lib.php';

cors(['GET', 'POST']);

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    exigir_admin();
    responder(db()->query('SELECT * FROM cadastros ORDER BY created_at DESC, id DESC')->fetchAll());
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') responder(['error' => 'Método não permitido'], 405);
$body = corpo_json();

if (($body['acao'] ?? '') === 'login') {
    $ok = hash_equals(strtolower($config['admin_email']), strtolower((string) ($body['email'] ?? '')))
        && password_verify((string) ($body['senha'] ?? ''), $config['admin_senha_hash']);
    if (!$ok) {
        sleep(1); // freia tentativa de senha por força bruta
        responder(['error' => 'E-mail ou senha incorretos'], 401);
    }
    responder(['token' => gerar_token()]);
}

if (($body['acao'] ?? '') === 'retry') {
    exigir_admin();
    $stmt = db()->prepare('SELECT * FROM cadastros WHERE id = ?');
    $stmt->execute([(int) ($body['id'] ?? 0)]);
    $c = $stmt->fetch();
    if (!$c) responder(['error' => 'Cadastro não encontrado'], 404);
    responder(processar($c));
}

responder(['error' => 'Ação inválida'], 400);
