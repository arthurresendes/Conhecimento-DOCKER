CREATE DATABASE IF NOT EXISTS flaskdocker;

USE flaskdocker;

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255),
    PRIMARY KEY (`id`)
);