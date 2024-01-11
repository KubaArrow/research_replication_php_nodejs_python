const http = require('http');
const mysql = require('mysql');

// Konfiguracja połączenia z bazą danych
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'yourUsername',
    password: 'yourPassword',
    database: 'yourDatabase'
});

connection.connect();

// Tworzenie serwera HTTP
http.createServer((req, res) => {
    // Wykonanie zapytania SELECT
    connection.query('SELECT * FROM yourTable', (error, results, fields) => {
        if (error) {
            res.writeHead(500, {'Content-Type': 'text/plain'});
            res.end('Server error');
            return;
        }

        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify(results));
    });
}).listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
