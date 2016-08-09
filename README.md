# Stampery Python
 Stampery API for Python. Notarize all your data using the blockchain!

# Usage
```python

from index import Stampery

stampery = Stampery('2d4cdee7-38b0-4a66-da87-c1ab05b43768', 'prod')

def ready():
    digest = stampery.hash("Hello, blockchain!")
    stampery.stamp(digest)

def proof(hash, aProof):
    print "\nReceived proof for \n%s \n\nProof\n%s" % (hash, aProof)

def error(err):
    print "\nWoot: %s" % err

stampery.on("error", error )
stampery.on("proof", proof )
stampery.on("ready", ready )

stampery.start()


 ```
## Installation
Coming soon

# Official implementations
- [NodeJS](https://github.com/stampery/node)
- [PHP](https://github.com/stampery/php)
- [Ruby](https://github.com/stampery/ruby)
- [Python](https://github.com/stampery/python)
- [Elixir](https://github.com/stampery/elixir)

# Feedback

Ping us at support@stampery.com and we’ll help you! 😃


## License

Code released under
[the MIT license](https://github.com/stampery/js/blob/master/LICENSE).

Copyright 2016 Stampery
