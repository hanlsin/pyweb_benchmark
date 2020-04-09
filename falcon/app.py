from wsgiref.simple_server import make_server

import falcon
from web3 import Web3

web3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/43d5d59eb1b5425f93a5acb2d334d9e2'))


class HelloWorld:
    def on_get(self, req, resp):
        resp.body = 'Hello World'


class Blocks:
    def on_get(self, req, resp):
        for i in range(1000):
            web3.eth.getBlock(200000)
        resp.body = 'retrieved 1000 blocks'


class Transactions:
    def on_get(self, req, resp):
        for i in range(1000):
            web3.eth.getBlock(200000, full_transactions=True)
        resp.body = 'retrieved 1000 blocks and all transactions of each'

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
