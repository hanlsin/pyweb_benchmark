
import sys

from flask import Flask
from web3 import Web3


app = Flask(__name__)
web3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/43d5d59eb1b5425f93a5acb2d334d9e2'))


@app.route('/hello')
def hello_world():
    return 'Hello World'


@app.route('/blocks')
def get_blocks():
    for i in range(1000):
        web3.eth.getBlock(200000)
        if i % 10 == 0:
            print(" ... {}th block".format(i))
    return 'retrieved 1000 blocks'


@app.route('/')
def root():
    return '<b>Hello, this is the root path of the server.</b>'


debug_mode = False
if len(sys.argv) > 1:
    debug_mode = True

# no necessary when to start using the 'flask' cli.
app.run(host='localhost', port=8080, debug=debug_mode)

