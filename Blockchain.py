from Block import Block
import time
import json
from hashlib import sha256
import MySQLdb
class Blockchain:
    def __init__(self):
        """
        Constructor của class `Blockchain`.
        """
        self.chain = [] 
        self.createGenesisBlock()

    def createGenesisBlock(self):
        GenesisBlock = Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7", 0)
        self.chain.append(GenesisBlock)

    #return Block object
    def getLatestBlock(self): 
        return self.chain[-1]

    def calculateHash(self, index, previousHash, timestamp, data, nonce):
        data = (str(index) + previousHash + 
        str(timestamp) + data + str(nonce)).encode('utf-8')
        
        return sha256(data).hexdigest()

    def generateNextBlock(self, blockData):
        prevBlock = self.getLatestBlock()
        nextIndex = prevBlock.index + 1
        timestamp = int(time.time()) 
        #nextHash = self.calculateHash(nextIndex, prevBlock.hashData, timestamp, blockData)
        #nextHash = 
        return self.proof_of_work(nextIndex, prevBlock.hashData, timestamp, blockData, nonce=0)

    def proof_of_work(self, index, previousHash, timestamp, data, nonce):
        """
        Hàm thử các giá trị khác nhau của nonce để lấy giá trị băm thỏa mãn
        """
        nonce = 0 
        computed_hash = self.calculateHash(index, previousHash, timestamp, data, nonce)
        while not computed_hash.startswith('0' * self.get_difficulty()):
            nonce += 1
            computed_hash = self.calculateHash(index, previousHash, timestamp, data, nonce)

        print('MINER NONCE: ')
        print(nonce)
        return Block(index, previousHash, timestamp, data, computed_hash, nonce)

    def display_chain(self):
        for block in self.chain:
            print("index: " + str(block.index))
            print("previous: " + str(block.previousHash))
            print("timestamp :" + str(block.timestamp))
            print("Transaction " + block.transaction)
            print("hash data: " + str(block.hashData))
            print('nonce: ' + str(block.nonce))
            
    def get_last_record(self):
        db_ = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",db="blockchain")
        db_.autocommit(True)
        db_cursor = db_.cursor()
        sql = "SELECT * FROM blocks ORDER by id DESC limit 1"
        db_cursor.execute(sql)
        result = db_cursor.fetchall()
        db_.commit() 

        for row in result:
            index = row[0]
            previousHash = row[1]
            timestamp = row[2]
            transaction = row[3]
            hashData = row[4]
            nonce = row[5]
        
        return Block(index, previousHash, timestamp, transaction, hashData, nonce) 

    def get_difficulty(self):
        db_ = MySQLdb.connect(
            host="localhost", 
            port=3306, 
            user="root", 
            passwd="",
            db="blockchain")
        db_.autocommit(True)
        db_cursor = db_.cursor()
        sql = "SELECT difficult FROM configs limit 1"
        db_cursor.execute(sql)
        result = db_cursor.fetchall()
        db_.commit() 
        for row in result:
            difficult = row[0]
        
        return difficult
        

bc = Blockchain()

bc.get_difficulty()
# bc.display_chain()

