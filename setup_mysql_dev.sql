-- database setup
-- user setup
create user if not exists 'hbnb_dev'@'localhost' identified by "hbnb_dev_pwd";
create database if not exists hbnb_dev_db;
use hbnb_dev_db;
grant all privileges on hbnb_dev_db.* to 'hbnb_dev'@'localhost';
use mysql;
grant select on perfomance_schema.* to 'hbnb_dev'@'localhost';
