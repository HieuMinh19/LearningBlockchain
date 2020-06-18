import eth_keys, os
import binascii
import MySQLdb

class TransactionOutput:
    def __init__(self, amount, tx_index, public_key, block_hash):
        """
        value: giá trị cổ phiếu giao dịch
        tx_index: index của transaction trong mảng
        script_sign: kịch bản khóa.
        """
        self.amount = amount
        self.tx_index = tx_index
        self.public_key = public_key
        self.block_hash = block_hash
    

message = b"lalala"
strPrivateKey = '0x426d4032eb945b3ae164273a073ea6159a0d9f3b34abc26c2379f27ce5cc31fc'

#
#print("start: ", strPrivateKey[2:].encode())
byteHexPriv = strPrivateKey[2:].encode()
bytePriv = binascii.unhexlify(byteHexPriv)
priv = eth_keys.keys.PrivateKey(bytePriv)
sig2 = priv.sign_msg(message)
#signerPubKey = priv.public_key
# print("sig2: ", sig2)
# print("end")


# recoveredPubKey = sig2.recover_public_key_from_msg(message)
# print('Recovered public key (128 hex digits):', recoveredPubKey)
# print('Public key correct? ', recoveredPubKey)
# valid = signerPubKey.verify_msg(message, sig2)
# print("Signature valid?", valid)



def get_by_signature(signature, msg, amount):
    publicKey = signature.recover_public_key_from_msg(msg)
    strPublicKey = str(publicKey)[2:]
    print('PUBLIC KEY', strPublicKey)
    db_ = MySQLdb.connect(
        host="localhost", 
        port=3306, 
        user="root", 
        passwd="", 
        db="blockchain")
    db_cursor = db_.cursor()
    sql = 'SELECT * FROM trans_output WHERE public_key = '
    sql += '"'
    sql += strPublicKey
    sql += '"'
    sql +=  " AND amount > "
    sql += str(amount)
    sql += " ORDER BY amount desc LIMIT 1"
    db_cursor.execute(sql)
    result = db_cursor.fetchall()
    if(db_cursor.rowcount):    
        for row in result:
            #id = row[0]
            totalAmount = row[1]
            txIndex = row[2]
            publicKey = row[3]
            blockHash = row[4]

        transOutput = TransactionOutput(totalAmount, txIndex, publicKey, blockHash)
        return transOutput
    else: return None


'''
create array transaction output and return uspend amount
@param: transOutput TransactionOutput Object
@param: float -> cost: total amount using
@param: String -> receiveUser: public Key receive user
@param: String -> selfHash: public Key your self
@param: String ->blockHash
@return: Object -> TransactionOutput
'''
def calculate_trans_output(transOutput, cost, receiveUser, selfHash, blockHash):
    result = []
    returnCost = transOutput.amount - cost
    transOutput = TransactionOutput(cost, 0, receiveUser, blockHash)
    returnTransOutput = TransactionOutput(returnCost, 1, selfHash, blockHash)
    result.append(transOutput)
    result.append(returnTransOutput)

    return result


trans = get_by_signature(sig2, message, 10)
hashData = '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7'
pubKey = '45349a48fc30078dc98e226a0bc50b6f814eec2c3cb479ac40c758dd5d6fac68c0f543d53e93dabeed8f7b517424f9514183eb13466f87a24ac872080c1f6f01'
result2 = calculate_trans_output(trans, 10, pubKey, pubKey, hashData)
print('RESULT 2', result2[0].amount)




