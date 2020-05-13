from Block import Block
import time
from hashlib import sha256
class main:
    blockchain = []
    def __init__(self, blockchain = []):
        super().__init__()
        self.blockchain = blockchain
    
    def getGenesisBlock(self):
        BlockClass = Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")
        self.blockchain.append(BlockClass)
    
    def getLatestBlock(self):
        # print(self.blockchain[len(self.blockchain) - 1])                
        return self.blockchain[len(self.blockchain) - 1]
    
    def generateNextBlock(self, blockData):
        prevBlock = self.getLatestBlock()
        nextIndex = prevBlock.index + 1
        timestamp = int(time.time()) 
        nextHash = self.calculateHash(nextIndex, prevBlock.hashData, timestamp, blockData)
        return Block(nextIndex, prevBlock.hashData, timestamp, blockData, nextHash)

    def calculateHash(self, index, previousHash, timestamp, data):
        data = (str(index) + previousHash + str(timestamp) + data).encode('utf-8')
        return sha256(data).hexdigest()

    def calculateHashForBlock(self, block):
        data = (str(block.index) + block.previousHash + str(block.timestamp) + block.transaction).encode('utf-8')
        return sha256(data).hexdigest()

    def isValidNewBlock(self, newBlock, previousBlock):
        if previousBlock.index + 1 != newBlock.index :
            print("invalid index")
            return False
        elif previousBlock.hashData != newBlock.previousHash :
                print("invalid previous block")
                return False
        elif self.calculateHashForBlock(newBlock) != newBlock.hashData :
                return False
        return True

    def addBlock(self, newBlock):
        if self.isValidNewBlock(newBlock, self.getLatestBlock()) :
            self.blockchain.append(newBlock)

main = main()
main.getGenesisBlock()
newBlock = main.generateNextBlock("xin chao cac ban")
main.addBlock(newBlock)
main.getLatestBlock()
""""main.getGenesisBlock()"""