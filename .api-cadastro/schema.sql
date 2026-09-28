-- Cadastros vindos de /cadastro/. Rodar uma vez no banco viskoo-cadastros.
CREATE TABLE IF NOT EXISTS cadastros (
  id              INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  nome            VARCHAR(255) NOT NULL,
  email           VARCHAR(255) NOT NULL,
  whatsapp        VARCHAR(50)  NOT NULL,
  empresa         VARCHAR(255) NOT NULL,
  documento       VARCHAR(30)  NOT NULL,
  rua             VARCHAR(255) NOT NULL,
  numero          VARCHAR(30)  NOT NULL,
  bairro          VARCHAR(255) NOT NULL,
  cep             VARCHAR(20)  NOT NULL,
  cidade          VARCHAR(255) NOT NULL,
  dia_pagamento   VARCHAR(30)  NOT NULL,
  descricao       TEXT         NOT NULL,
  valor           VARCHAR(50)  NOT NULL,
  parcelamento    VARCHAR(100) NOT NULL,
  status          ENUM('pendente', 'sincronizado', 'erro') NOT NULL DEFAULT 'pendente',
  asaas_id        VARCHAR(50)  NULL,
  erro            TEXT         NULL,
  sincronizado_em DATETIME     NULL,
  INDEX cadastros_created_at_idx (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
