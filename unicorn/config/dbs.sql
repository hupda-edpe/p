CREATE USER 'eap'@'%' IDENTIFIED BY '123456';
GRANT USAGE ON *.* TO 'eap'@'%' REQUIRE NONE;

CREATE DATABASE IF NOT EXISTS eap_testing;
CREATE DATABASE IF NOT EXISTS eap_development;

GRANT ALL PRIVILEGES ON eap_testing.* TO 'eap'@'%';
GRANT ALL PRIVILEGES ON eap_development.* TO 'eap'@'%';
GRANT ALL PRIVILEGES ON `eap\_%`.* TO 'eap'@'%';
