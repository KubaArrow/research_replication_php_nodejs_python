import tornado.ioloop
import tornado.web
import mysql.connector

# Konfiguracja połączenia z bazą danych
db_connection = mysql.connector.connect(
    host='localhost',
    user='yourUsername',
    password='yourPassword',
    database='yourDatabase'
)

# Klasa obsługująca zapytanie HTTP
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            # Tworzenie kursora do bazy danych
            cursor = db_connection.cursor()

            # Wykonanie zapytania SELECT
            cursor.execute('SELECT * FROM yourTable')

            # Pobranie wyników zapytania
            results = cursor.fetchall()

            # Zamknięcie kursora
            cursor.close()

            # Wysłanie wyników jako odpowiedź HTTP
            self.write({'data': results})
        except Exception as e:
            self.set_status(500)
            self.write({'error': 'Server error'})

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    print('Server running at http://localhost:3000/')
    tornado.ioloop.IOLoop.current().start()
