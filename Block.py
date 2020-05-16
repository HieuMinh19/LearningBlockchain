from hashlib import sha256
class Block:
    def __init__(self, index, previousHash, timestamp, transaction, hashData, nonce):
        """
        Constructor cho một `Block` class.
        :param index: Chỉ số ID duy nhất của một block.
        :param previousHash: Chỉ số khối trước đó.
        :param timestamp: Thời gian tạo block.
        """
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.transaction = transaction
        self.hashData = hashData
        self.nonce = nonce

    def calculateHashForBlock(self):
        data = (str(self.index) + self.previousHash + 
        str(self.timestamp) + self.transaction + str(self.nonce)).encode('utf-8')
        self.hashData = sha256(data).hexdigest()
        return self.hashData