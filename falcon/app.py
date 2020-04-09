from wsgiref.simple_server import make_server

import falcon


class HelloWorld:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = 'Hello World'


app = falcon.App()
app.add_route('/tests/hello-world', HelloWorld())

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
