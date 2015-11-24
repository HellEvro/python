Stampery
=======
[![PyPI version](https://badge.fury.io/py/stampery.svg)](https://badge.fury.io/py/stampery)

Notarize all your data using the blockchain. Generate immutable and valid globally proofs of existence, integrity and ownership of any piece of data.

## Get Started

```
pip install stampery
```

```python
import stampery
stampery = Stampery('830fa1bf-bee7-4412-c1d3-31dddba2213d')
```

### Arbitrary object stamping
```python
stampery.stamp({'meta': 'data'})
```
### File stamping
```python
file = open('/Users/user/Desktop/Artboard 2.png', 'rb')

stampery.stamp({'meta': 'data'}, file)
```
### Getting a stamp
```python
stampery.get(hash)
```

You can get your API key [signing up](https://stampery.com/signup) and going to [your account](https://stampery.com/account) -> Apps.

## License

Code released under [the MIT license](https://github.com/stampery/node/blob/master/LICENSE).

Copyright 2015 Stampery
