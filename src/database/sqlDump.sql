/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS bill;
CREATE TABLE `bill` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `bill_sub_total` double NOT NULL,
  `bill_discount_applied` double NOT NULL,
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS discounts;
CREATE TABLE `discounts` (
  `discount_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_id` int DEFAULT NULL,
  `discount_name` varchar(255) DEFAULT NULL,
  `discount_start` date DEFAULT NULL,
  `discount_end` date DEFAULT NULL,
  `discount_value` float DEFAULT NULL,
  PRIMARY KEY (`discount_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `discounts_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS employee;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_id` int DEFAULT NULL,
  `employee_name` varchar(64) NOT NULL,
  `employee_account_type` varchar(64) NOT NULL,
  `employee_password` varchar(256) NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS inventory;
CREATE TABLE `inventory` (
  `inventory_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_id` int DEFAULT NULL,
  `inventory_item_name` varchar(64) NOT NULL,
  `inventory_item_stock` int NOT NULL,
  `inventory_item_reorder_level` int NOT NULL,
  `inventory_item_type` varchar(64) NOT NULL,
  `is_available` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`inventory_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS inventory_restaurant;
CREATE TABLE `inventory_restaurant` (
  `restaurant_id` int DEFAULT NULL,
  `inventory_id` int DEFAULT NULL,
  KEY `restaurant_id` (`restaurant_id`),
  KEY `inventory_id` (`inventory_id`),
  CONSTRAINT `inventory_restaurant_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`),
  CONSTRAINT `inventory_restaurant_ibfk_2` FOREIGN KEY (`inventory_id`) REFERENCES `inventory` (`inventory_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS menu;
CREATE TABLE `menu` (
  `menu_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_id` int DEFAULT NULL,
  `menu_item_name` varchar(64) NOT NULL,
  `menu_item_category` varchar(64) NOT NULL,
  `menu_item_notes` varchar(64) DEFAULT NULL,
  `menu_item_price` float DEFAULT NULL,
  `is_available` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`menu_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS menu_ingredients;
CREATE TABLE `menu_ingredients` (
  `menu_id` int NOT NULL,
  `restaurant_id` int DEFAULT NULL,
  `inventory_id` int NOT NULL,
  `inventory_qty_needed` int NOT NULL,
  PRIMARY KEY (`menu_id`,`inventory_id`),
  KEY `inventory_id` (`inventory_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `menu_ingredients_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`menu_id`),
  CONSTRAINT `menu_ingredients_ibfk_2` FOREIGN KEY (`inventory_id`) REFERENCES `inventory` (`inventory_id`),
  CONSTRAINT `menu_ingredients_ibfk_3` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS orders;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_table_num` int NOT NULL,
  `order_status` varchar(64) NOT NULL,
  `order_menu_item` varchar(64) NOT NULL,
  `order_menu_item_qty` varchar(64) NOT NULL,
  `order_menu_item_desc` varchar(64) NOT NULL,
  `order_author` varchar(64) NOT NULL,
  `order_time_created` datetime NOT NULL,
  `order_price` varchar(64) NOT NULL,
  `bill_id` int DEFAULT NULL,
  `restaurant_id` int DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `bill_id` (`bill_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bill` (`bill_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS reservation;
CREATE TABLE `reservation` (
  `reservation_id` int NOT NULL AUTO_INCREMENT,
  `reservation_customer_name` varchar(64) NOT NULL,
  `reservation_customer_phone` varchar(11) NOT NULL,
  `reservation_party_size` int NOT NULL,
  `reservation_author` varchar(64) NOT NULL,
  `reservation_creation_time` datetime NOT NULL,
  `reservation_date` date NOT NULL,
  `reservation_time` time NOT NULL,
  `table_id` int DEFAULT NULL,
  `restaurant_id` int DEFAULT NULL,
  PRIMARY KEY (`reservation_id`),
  KEY `table_id` (`table_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`table_id`) REFERENCES `tables` (`table_id`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS restaurant;
CREATE TABLE `restaurant` (
  `restaurant_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_location` varchar(64) NOT NULL,
  `restaurant_name` varchar(64) NOT NULL,
  `restaurant_capacity` int NOT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS tables;
CREATE TABLE `tables` (
  `table_id` int NOT NULL AUTO_INCREMENT,
  `table_number` int NOT NULL,
  `table_capacity` int NOT NULL,
  `restaurant_id` int DEFAULT NULL,
  PRIMARY KEY (`table_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `tables_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO restaurant(restaurant_id,restaurant_location,restaurant_name,restaurant_capacity) VALUES('1','\'BRISTOL\'','\'Bristol 1\'','6'),('2','\'BRISTOL\'','\'Bristol 2\'','6'),('3','\'BIRMINGHAM\'','\'Birmingham 1\'','6'),('4','\'BIRMINGHAM\'','\'Birmingham 2\'','6'),('5','\'CARDIFF\'','\'Cardiff 1\'','6'),('6','\'CARDIFF\'','\'Cardiff 2\'','6'),('7','\'GLASGOW\'','\'Glasgow 1\'','6'),('8','\'GLASGOW\'','\'Glasgow 2\'','6'),('9','\'MANCHESTER\'','\'Manchester 1\'','6'),('10','\'MANCHESTER\'','\'Manchester 2\'','6'),('11','\'NOTTINGHAM\'','\'Nottingham 1\'','6'),('12','\'NOTTINGHAM\'','\'Nottingham 2\'','6'),('13','\'LONDON\'','\'London 1\'','6'),('14','\'LONDON\'','\'London 2\'','6');

INSERT INTO bill(bill_id,bill_sub_total,bill_discount_applied) VALUES('1','90.95','0'),('2','74.95','0'),('3','22.989999999999995','0'),('4','0','0'),('5','0','0'),('6','0','0');

INSERT INTO discounts(discount_id, restaurant_id, discount_name, discount_start, discount_end, discount_value) 
VALUES
('1', '3', 'New Year''s', '2024-01-07', '2024-01-31', '15'),
('2', '2', 'New Year''s', '2024-01-07', '2024-01-31', '15'),
('3', '1', 'New Year''s', '2024-01-07', '2024-01-31', '15');

INSERT INTO employee (employee_password, employee_name, employee_account_type,restaurant_id)
VALUES
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','1'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','2'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','3'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','4'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','5'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','6'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','7'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','8'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','9'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','10'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','11'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','12'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','13'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Adam Min','ADMIN', '14'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Che Fu', 'CHEF','14'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Deren Ter', 'DIRECTOR','14'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Kim Chin', 'KITCHEN','14'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Fred Staf', 'FRONT','14'),
    ('$5$rounds=535000$ZJzrW.k1Fti1F.FA$gI4g6OBdx/jBZ.tFRbCsoyGFwVzP1kUbs2eBHiMuIW.', 'Man Ager', 'MANAGER','14');
INSERT INTO inventory(inventory_id,restaurant_id,inventory_item_name,inventory_item_stock,inventory_item_reorder_level,inventory_item_type,is_available) VALUES('1','1','\'Spaghetti\'','0','10','\'Mains\'','1'),('2','1','\'Ice-cream\'','5','10','\'Desert\'','1'),('3','1','\'Lemonade\'','0','10','\'Drinks\'','1'),('4','2','\'Grilled Salmon\'','3','10','\'Mains\'','1'),('5','2','\'Chocolate Lava Cake\'','7','10','\'Deserts\'','1'),('6','2','\'Milkshake\'','20','10','\'Drinks\'','1'),('7','3','\'Spaghetti\'','10','2','\'Mains\'','1'),('8','3','\'Icecream\'','10','2','\'Deserts\'','1'),('9','3','\'Lemonate\'','10','2','\'Drinks\'','1');


INSERT INTO menu(menu_id, restaurant_id, menu_item_name, menu_item_category, menu_item_notes, menu_item_price, is_available) 
VALUES
('1', '1', 'Spaghetti', 'Mains', 'Contains: Gluten - Pasta with tomato sauce', '12.99', '1'),
('2', '1', 'Ice-cream', 'Desert', 'Contains: Milk - Cold vanilla chilled and topped with chocolate', '8', '1'),
('3', '1', 'Lemonade', 'Drinks', 'Sweet refreshing summer drink', '2', '1'),
('4', '2', 'Grilled Salmon', 'Mains', 'Contains: Fish,Dairy - Cooked Salmon with butter', '15.99', '1'),
('5', '2', 'Chocolate Lava Cake', 'Deserts', 'Contains: Milk, Eggs - Gooey molten chocolate cake', '12.99', '1'),
('6', '2', 'Milkshake', 'Drinks', 'Contains: Milk - Chocolate milkshake', '8.99', '1'),
('7', '3', 'Spaghetti', 'Mains', 'Contains: Gluten - Pasta with tomato sauce', '12.99', '1'),
('8', '3', 'Icecream', 'Deserts', 'Contains: Milk - Vanilla ice cream', '8', '1'),
('9', '3', 'Lemonate', 'Drinks', 'Cold Lemonade with ice', '2', '1');


INSERT INTO orders(order_id, order_table_num, order_status, order_menu_item, order_menu_item_qty, order_menu_item_desc, order_author, order_time_created, order_price, bill_id, restaurant_id) 
VALUES
('1', '1', 'COMPLETED', 'Spaghetti', '5', '', '1', '2024-01-07 20:05:29', '12.99', '1', '1'),
('2', '1', 'COMPLETED', 'Ice-cream', '2', '', '1', '2024-01-07 20:05:29', '8.0', '1', '1'),
('3', '1', 'COMPLETED', 'Lemonade', '5', '', '1', '2024-01-07 20:05:29', '2.0', '1', '1'),
('4', '1', 'COMPLETED', 'Spaghetti', '5', '', '1', '2024-01-07 20:05:46', '12.99', '2', '1'),
('5', '1', 'COMPLETED', 'Ice-cream', '0', '', '1', '2024-01-07 20:05:46', '8.0', '2', '1'),
('6', '1', 'COMPLETED', 'Lemonade', '5', '', '1', '2024-01-07 20:05:46', '2.0', '2', '1'),
('7', '1', 'COMPLETED', 'Spaghetti', '1', '', '1', '2024-01-07 20:05:53', '12.99', '3', '1'),
('8', '1', 'COMPLETED', 'Ice-cream', '0', '', '1', '2024-01-07 20:05:53', '8.0', '3', '1'),
('9', '1', 'COMPLETED', 'Lemonade', '5', '', '1', '2024-01-07 20:05:53', '2.0', '3', '1'),
('10', '1', 'COMPLETED', 'Spaghetti', '0', '', '1', '2024-01-07 20:06:31', '12.99', '4', '1'),
('11', '1', 'COMPLETED', 'Ice-cream', '0', '', '1', '2024-01-07 20:06:31', '8.0', '4', '1'),
('12', '1', 'COMPLETED', 'Lemonade', '0', '', '1', '2024-01-07 20:06:31', '2.0', '4', '1'),
('13', '1', 'COMPLETED', 'Spaghetti', '0', '', '1', '2024-01-07 20:07:04', '12.99', '5', '1'),
('14', '1', 'COMPLETED', 'Ice-cream', '0', '', '1', '2024-01-07 20:07:04', '8.0', '5', '1'),
('15', '1', 'COMPLETED', 'Lemonade', '0', '', '1', '2024-01-07 20:07:04', '2.0', '5', '1'),
('16', '1', 'COMPLETED', 'Spaghetti', '0', '', '1', '2024-01-07 20:07:32', '12.99', '6', '1'),
('17', '1', 'COMPLETED', 'Ice-cream', '0', '', '1', '2024-01-07 20:07:32', '8.0', '6', '1'),
('18', '1', 'COMPLETED', 'Lemonade', '0', '', '1', '2024-01-07 20:07:32', '2.0', '6', '1');





INSERT INTO tables(table_id,table_number,table_capacity,restaurant_id) VALUES('1','1','2','1'),('2','2','4','1'),('3','3','6','1'),('4','4','8','1'),('5','5','6','1'),('6','6','6','1'),('7','1','2','2'),('8','2','4','2'),('9','3','6','2'),('10','4','8','2'),('11','5','6','2'),('12','6','6','2'),('13','1','2','3'),('14','2','4','3'),('15','3','6','3'),('16','4','8','3'),('17','5','6','3'),('18','6','6','3'),('19','1','2','4'),('20','2','4','4'),('21','3','6','4'),('22','4','8','4'),('23','5','6','4'),('24','6','6','4'),('25','1','2','5'),('26','2','4','5'),('27','3','6','5'),('28','4','8','5'),('29','5','6','5'),('30','6','6','5'),('31','1','2','6'),('32','2','4','6'),('33','3','6','6'),('34','4','8','6'),('35','5','6','6'),('36','6','6','6'),('37','1','2','7'),('38','2','4','7'),('39','3','6','7'),('40','4','8','7'),('41','5','6','7'),('42','6','6','7'),('43','1','2','8'),('44','2','4','8'),('45','3','6','8'),('46','4','8','8'),('47','5','6','8'),('48','6','6','8'),('49','1','2','9'),('50','2','4','9'),('51','3','6','9'),('52','4','8','9'),('53','5','6','9'),('54','6','6','9'),('55','1','2','10'),('56','2','4','10'),('57','3','6','10'),('58','4','8','10'),('59','5','6','10'),('60','6','6','10'),('61','1','2','11'),('62','2','4','11'),('63','3','6','11'),('64','4','8','11'),('65','5','6','11'),('66','6','6','11'),('67','1','2','12'),('68','2','4','12'),('69','3','6','12'),('70','4','8','12'),('71','5','6','12'),('72','6','6','12'),('73','1','2','13'),('74','2','4','13'),('75','3','6','13'),('76','4','8','13'),('77','5','6','13'),('78','6','6','13'),('79','1','2','14'),('80','2','4','14'),('81','3','6','14'),('82','4','8','14'),('83','5','6','14'),('84','6','6','14');