To check available mysql images
```
docker search mysql
```

To pull the latest mysql images
```
docker pull mysql
docker image ls
```

To start the mysql container
```
docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
```

Goes to the container of mysql
```
docker container ls
docker exec -ti <container_id> /bin/bash
mysql -h localhost -u root -p
```

Basic command of mysql
```
SHOW databases;
CREATE DATABASE techbow;
USE techbow;
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    PRIMARY KEY ( `id` ),
    INDEX NAME_IND (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX NAME_IND ON user (name);
SHOW tables;
DESC user;
INSERT INTO user (name, email) VALUES ("A", "a@gmail.com");
SELECT * FROM use WHERE name = 'A';
```

To build the image contains the web app
```
docker build -t web-mysql:v1 .
```

To check the image we just build
```
docker image ls
```

Deploy a docker contains the web app.
```
docker run -p 5000:5000 --link mysql:mysql-host -d --name web-mysql web-mysql:v1
```

Check the host setting in webapp from docker container.
```
docker exec -ti <container_id> /bin/bash
cat /etc/hosts
```
