CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    PRIMARY KEY(id)
);

INSERT INTO employees (name, age) VALUES ('John Doe', 30);
INSERT INTO employees (name, age) VALUES ('Jane Doe', 25);