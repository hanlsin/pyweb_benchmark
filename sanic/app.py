from sanic import Sanic
from sanic.response import text
from web3 import Web3

app = Sanic(name='sanic_benchmark')
web3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/43d5d59eb1b5425f93a5acb2d334d9e2'))


@app.get('/hello-world')
async def hello_world(request):
    return text('Hello World')


@app.get('/blocks')
async def get_blocks(request):
    for i in range(1000):
        web3.eth.getBlock(200000)
    return text('retrieved 1000 blocks')


@app.get('/transactions')
async def get_transactions(request):
    for i in range(1000):
        web3.eth.getBlock(200000, full_transactions=True)
    return text('retrieved 1000 blocks and all transactions of each')


@app.post('/transactions')
async def send_transactions(request):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
