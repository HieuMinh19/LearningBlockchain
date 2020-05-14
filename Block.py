from hashlib import sha256
class Block:
    def __init__(self, index, previousHash, timestamp, transaction, hashData):
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
        
    # def getGenesisBlock(self):
    #     BlockClass = Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")
    #     return BlockClass
    
    def calculateHashForBlock(self):
        data = (str(self.index) + self.previousHash + str(self.timestamp) + self.transaction).encode('utf-8')
        self.hashData = sha256(data).hexdigest()
        return self.hashData