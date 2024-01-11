-- Tworzenie tabeli 'myTable'
CREATE TABLE myTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    value INT NOT NULL
);

-- Wstawianie przykładowych danych
INSERT INTO myTable (name, value) VALUES ('Item1', 100);
INSERT INTO myTable (name, value) VALUES ('Item2', 150);
INSERT INTO myTable (name, value) VALUES ('Item3', 200);
INSERT INTO myTable (name, value) VALUES ('Item4', 250);
