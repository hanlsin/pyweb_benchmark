# pyweb_benchmark
This is for benchmark testing Python web frameworks for a blockchain

## Version
* Python: 3.7

## Web frameworks
* [Flask](https://github.com/pallets/flask)
* [Sanic](https://github.com/huge-success/sanic)
* [Bottle](https://github.com/bottlepy/bottle) version 0.12(stable) at 2020-04-09
* [Falcon](https://github.com/falconry/falcon)

## Blockchain
We are testing a testnet, so it may be a different performance with a mainnet.

### Ethereum Testnet
* Ropsten: HttpProvider ('https://ropsten.infura.io')

### Aergo
TBD

## Test cases

### Case 1.
Performance test for getting 1000 blocks by 100 sessions concurrently.

### Case 2.
Performance test for getting all transactions of 1000 blocks by 100 sessions concurrently.
The block range would be fixed for checking same transactions by all frameworks.

### Case 3.
Performance test for sending 100 transactions by 100 sessions concurrently.
All payloads of transactions would be fixed for providing same network size.

## Environment
We are using `pipenv` as a default virtual environment tool.

### Start virtual env
Please check the default python version above to make a proper virtual environment.

```
pipenv shell
```
