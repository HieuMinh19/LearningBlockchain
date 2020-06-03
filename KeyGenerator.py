from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey


# Generate new Keys
privateKey = PrivateKey()
print('PRIVATE KEY', privateKey.toString())
publicKey1 = privateKey.publicKey()
publicKey2 = privateKey.publicKey()
print('PUBLIC1', publicKey1)
print('PUBLIC2', publicKey2.toString())

message = "My test message"

# Generate Signature
signature = Ecdsa.sign(message, privateKey)
print('SIGNATURE', signature)
# To verify if the signature is valid
print(Ecdsa.verify(message, signature, publicKey1))

    