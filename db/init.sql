CREATE TABLE IF NOT EXISTS products (
  prd_id INT AUTO_INCREMENT PRIMARY KEY,
  code CHAR(13) NOT NULL,
  name VARCHAR(50) NOT NULL,
  item_code VARCHAR(20) NOT NULL,
  price_tax_included INT NOT NULL,
  UNIQUE KEY uq_products_code (code)
);
CREATE TABLE IF NOT EXISTS trades (
  trd_id BIGINT AUTO_INCREMENT PRIMARY KEY,
  datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  emp_cd CHAR(10) NOT NULL,
  store_cd CHAR(5) NOT NULL,
  pos_no CHAR(3) NOT NULL,
  total_amt_tax_included INT NOT NULL,
  total_amt_ex_tax INT NOT NULL
);
CREATE TABLE IF NOT EXISTS trade_items (
  dtl_id BIGINT AUTO_INCREMENT PRIMARY KEY,
  trd_id BIGINT NOT NULL,
  prd_id INT NOT NULL,
  prd_code CHAR(13) NOT NULL,
  prd_name VARCHAR(50) NOT NULL,
  prd_price_tax_included INT NOT NULL,
  tax_cd CHAR(2) NOT NULL DEFAULT '10',
  quantity INT NOT NULL DEFAULT 1,
  line_total_tax_included INT NOT NULL,
  CONSTRAINT fk_items_trade FOREIGN KEY (trd_id) REFERENCES trades(trd_id),
  CONSTRAINT fk_items_product FOREIGN KEY (prd_id) REFERENCES products(prd_id)
);
INSERT INTO products (code, name, item_code, price_tax_included) VALUES
('4901681349715','P-BAS86-BK/軸色・ブラック/インク色・黒','349701',1650),
('4901681349784','P-BAS86-WR/軸色・ワイン/インク色・黒','349718',1650),
('4901681349791','P-BAS86-BG/軸色・ブルーグリーン/インク色・黒','349719',1650),
('4901681349777','P-BAS86-P/軸色・ピンク/インク色・黒','349707',1650),
('4901681349746','P-BAS86-BE/軸色・ベージュ/インク色・黒','349713',1650),
('4901681349760','P-BAS86-W/軸色・ホワイト/インク色・黒','349715',1650)
ON DUPLICATE KEY UPDATE name=VALUES(name), item_code=VALUES(item_code), price_tax_included=VALUES(price_tax_included);
