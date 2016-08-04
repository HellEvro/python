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
