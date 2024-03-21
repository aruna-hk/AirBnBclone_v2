-- test database setup
-- user setup
create user if not exists 'hbnb_test'@'localhost' identified by "hbnb_test_pwd";
create database if not exists hbnb_test_db;
use hbnb_dev_db;
grant all privileges on hbnb_test_db.* to 'hbnb_test'@'localhost';
use mysql;
grant select on perfomance_schema.* to 'hbnb_test'@'localhost';
