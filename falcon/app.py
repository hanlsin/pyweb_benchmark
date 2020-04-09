from wsgiref.simple_server import make_server

import falcon


class HelloWorld:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = 'Hello World'


class Blocks:
    def on_get(self, req, resp):
        pass


class Transactions:
    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass


app = falcon.API()
app.add_route('/hello-world', HelloWorld())
app.add_route('/blocks', Blocks())
app.add_route('/transactions', Transactions())

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
