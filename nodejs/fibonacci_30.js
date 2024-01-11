const http = require('http');
const url = require('url');

function fibonacci(n) {
    let a = 0, b = 1, temp;

    while (n > 0) {
        temp = a;
        a = a + b;
        b = temp;
        n--;
    }

    return a;
}

http.createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;
    const n = 30;

    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Fibonacci of ' + n + ' is ' + fibonacci(n));

}).listen(3000);

console.log('Server running at http://localhost:3000/');
