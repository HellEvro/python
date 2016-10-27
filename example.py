from stampery import Stampery

# Sign up and get your secret token at https://api-dashboard.stampery.com
client = Stampery('user-secret')


def on_ready():
    digest = client.hash("Hello, blockchain!")
    client.stamp(digest)


def on_proof(hash, proof):
    print("Received proof for {}\n".format(hash))
    print("Proof\nVersion: {}\nSiblings: {}\nRoot: {}".format(
        proof['version'], proof['siblings'], proof['root']))
    print("Anchor:\n  Chain: {}\n  Tx: {}\n".format(
        proof['anchor']['chain'], proof['anchor']['tx']))

def on_error(err):
    print("Woot: " + err)

client.on("error", on_error)
client.on("proof", on_proof)
client.on("ready", on_ready)

client.start()
