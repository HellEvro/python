from index import Stampery

stampery = Stampery('2d4cdee7-38b0-4a66-da87-c1ab05b43768', 'prod')

def on_ready():
    digest = stampery.hash("Hello, blockchain!")
    stampery.stamp(digest)

def on_proof(hash, proof):
    print "Received proof for"
    print hash
    print "Proof"
    print proof

def on_error(err):
    print "Woot: %s" % err

stampery.on("error", on_error )
stampery.on("proof", on_proof )
stampery.on("ready", on_ready )

stampery.start()
