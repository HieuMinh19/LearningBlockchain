from Block import Block
import json
class Blockchain:
    difficulty = 2
    def __init__(self):
        """
        Constructor của class `Blockchain`.
        """
        self.chain = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        GenesisBlock = Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")
        self.chain.append(GenesisBlock)

    def getLastBlock(self):
        json.dumps(self.chain, separators=(',', ':'))
        # print("chain")
        # print(self.chain[0].transaction) 
        return self.chain[-1]

Blockchain = Blockchain()
Blockchain.getLastBlock()  