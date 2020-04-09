from sanic import Sanic
from sanic.response import text

app = Sanic(name='sanic_benchmark')


@app.get('/hello-world')
async def hello_world(request):
    return text('Hello World')


@app.get('/blocks')
async def get_blocks(request):
    pass


@app.get('/transactions')
async def get_transactions(request):
    pass


@app.post('/transactions')
async def send_transactions(request):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
