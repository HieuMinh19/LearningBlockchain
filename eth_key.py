import eth_keys, os
import binascii

def get_signature():
    private_key = '0xaf31e94431e76776cdd90c0351baa2a223beeddf127c5dd267b920ac4348e168'
    signature = eth_keys.keys.validate_private_key_bytes(private_key)
    print(signature) 

#       get_signature()

# Generate the private + public key pair (using the secp256k1 curve)
message = b"lalal"
signerPrivKey = eth_keys.keys.PrivateKey(os.urandom(32))
sig1 = signerPrivKey.sign_msg(message)


willSaveThisToFile = signerPrivKey.to_hex()
#
hexPriv = binascii.hexlify(signerPrivKey.to_bytes()).decode()
signerPubKey = signerPrivKey.public_key

print("start: ", willSaveThisToFile[2:].encode())
byteHexPriv = willSaveThisToFile[2:].encode()
bytePriv = binascii.unhexlify(byteHexPriv)
priv = eth_keys.keys.PrivateKey(bytePriv)
sig2 = priv.sign_msg(message)
print("sig1: ", sig1)
print("sig2: ", sig2)
print("end")
#

print('Private key (64 hex digits):', hex(signerPrivKey))
print('Private key (64 hex digits):', signerPrivKey.to_hex())
print('Public key (uncompressed, 128 hex digits):', signerPubKey)

# ECDSA sign message (using the curve secp256k1 + Keccak-256)
msg = b'Message for signing'
signature = signerPrivKey.sign_msg(msg)
print('Message:', msg)
print('Signature: [r = {0}, s = {1}, v = {2}]'.format(
    hex(signature.r), hex(signature.s), hex(signature.v)))

# ECDSA public key recovery from signature + verify signature
# (using the curve secp256k1 + Keccak-256 hash)
msg = b'Message for signing'
recoveredPubKey = signature.recover_public_key_from_msg(msg)
print('Recovered public key (128 hex digits):', recoveredPubKey)
print('Public key correct?', recoveredPubKey == signerPubKey)
valid = signerPubKey.verify_msg(msg, signature)
print("Signature valid?", valid)






