import asyncio
import tornado

def fibonacci(n):
    a = 0 
    b = 1 
    temp=None

    while n > 0:
        temp = a
        a = a + b
        b = temp
        n-=1
    return a


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n=30
        self.write('Fibonacci of ' + n + ' is ' + fibonacci(n))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())