from Block import Block
import time


class Blockchain:
    size = 0
    last_hash = ''
    last_block = None
    blocks = None

    def __init__(self):
        # generate genesis block
        ts = time.time()
        block = Block(ts, "This is Genesis Block", self.last_hash)
        self.blocks = block
        self.last_block = block
        self.last_hash = block.hash
        self.size += 1

    def addBlock(self, data):
        ts = time.time()
        block = Block(ts, data, self.last_hash)
        self.last_block.next = block
        self.last_block = block
        self.last_hash = block.hash
        self.size += 1

    def logAllBlock(self):
        # inner loop
        def loop_block(block):
            print(block.data)
            if block.next is not None:
                loop_block(block.next)

        loop_block(self.blocks)


blockchain = Blockchain()
blockchain.addBlock('First block')
blockchain.addBlock('Second block')
blockchain.addBlock('Third block')
blockchain.logAllBlock()
