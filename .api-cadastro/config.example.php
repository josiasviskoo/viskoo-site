<?php
// Copie para config.php no servidor e preencha. config.php NUNCA vai para o git.
return [
    'db_host' => 'localhost',
    'db_name' => 'viskoo-cadastros',
    'db_user' => 'viskoo-cadastros',
    'db_pass' => '',

    // Sandbox: https://api-sandbox.asaas.com/v3 — Produção: https://api.asaas.com/v3
    'asaas_base_url' => 'https://api.asaas.com/v3',
    'asaas_api_key'  => '',

    // Login do /cadastro/admin/. Gere o hash com: php -r "echo password_hash('SENHA', PASSWORD_DEFAULT);"
    'admin_email'      => 'josiasviskoo@gmail.com',
    'admin_senha_hash' => '',

    // Segredo aleatório para assinar o token do admin: php -r "echo bin2hex(random_bytes(32));"
    'token_secret' => '',

    'origens' => ['https://viskoo.com.br', 'https://www.viskoo.com.br'],
];
