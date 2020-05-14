from Block import Block
import time
from Blockchain import Blockchain
from hashlib import sha256
class main:
    chain = Blockchain()
    def __init__(self):
        super().__init__()
    
    def calculateHash(self, index, previousHash, timestamp, data):
        data = (str(index) + previousHash + str(timestamp) + data).encode('utf-8')
        return sha256(data).hexdigest()

    def isValidNewBlock(self, newBlock, previousBlock):
        if previousBlock.index + 1 != newBlock.index :
            print("invalid index")
            return False
        elif previousBlock.hashData != newBlock.previousHash :
                print("invalid previous block")
                return False
        elif newBlock.calculateHashForBlock() != newBlock.hashData :
                return False
        return True

    def addBlock(self, newBlock):
        if self.isValidNewBlock(newBlock, chain.getLatestBlock()) :
            #self.blockchain.append(newBlock)
            chain.chain.append(newBlock)

main = main()
chain = Blockchain()
newBlock = chain.generateNextBlock('i am Le Minh Hieu')
main.addBlock(newBlock)
lastBlock = chain.getLatestBlock()
print(lastBlock.transaction)   