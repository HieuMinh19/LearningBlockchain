from Block import Block
import time
class main:
    blockchain = []
    def __init__(self, blockchain = []):
        super().__init__()
        self.blockchain = blockchain
    
    def getGenesisBlock(self):
        BlockClass = Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")
        self.blockchain.append(BlockClass)
    
    def getLatestBlock(self):
        return self.blockchain[len(self.blockchain) - 1]
    
    def generateNextBlock(self):
        prevBlock = self.getLatestBlock()
        nextIndex = prevBlock.index + 1
        timestamp = int(time.time()) 
        print(timestamp)
        print(nextIndex)


main = main()
main.getGenesisBlock()
main.generateNextBlock()
""""main.getGenesisBlock()"""