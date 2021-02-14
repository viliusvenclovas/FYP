CREATE DATABASE if not exists project;

CREATE TABLE if not exists project.data(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  last_watered VARCHAR(88) NOT NULL
);