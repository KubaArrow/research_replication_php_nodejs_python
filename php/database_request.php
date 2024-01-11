<?php
$servername = "localhost"; // adres serwera
$username = "username"; // nazwa użytkownika
$password = "password"; // hasło
$dbname = "myDB"; // nazwa bazy danych

// Utworzenie połączenia
$conn = new mysqli($servername, $username, $password, $dbname);

// Sprawdzenie połączenia
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT name, value FROM myTable"; // Zapytanie SQL
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Wyświetlenie danych każdego wiersza
    while($row = $result->fetch_assoc()) {
        echo  "Name: " . $row["name"]. " - Value: " . $row["value"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
