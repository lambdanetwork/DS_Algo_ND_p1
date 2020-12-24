from Block import Block
import time
import unittest


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


# Unit test
class Testing(unittest.TestCase):
    def testGenesisBlock(self):
        blockchain = Blockchain()
        self.assertEqual(blockchain.blocks.data, "This is Genesis Block")
        self.assertEqual(blockchain.size, 1)
        self.assertEqual(blockchain.last_hash, blockchain.blocks.hash)

    def testNegativeCaseData(self):
        blockchain = Blockchain()
        blockchain.addBlock('First block')
        blockchain.addBlock('Second block')
        blockchain.addBlock('Third block')
        self.assertNotEqual(blockchain.blocks.next.data, 'Second block')
        self.assertNotEqual(blockchain.blocks.next.next.data, 'Third block')

    def testBlockchainDataIsAccurate(self):
        blockchain = Blockchain()
        blockchain.addBlock('First block')
        blockchain.addBlock('Second block')
        blockchain.addBlock('Third block')
        self.assertEqual(blockchain.blocks.next.data, 'First block')
        self.assertEqual(blockchain.blocks.next.next.data, 'Second block')
        self.assertEqual(blockchain.blocks.next.next.next.data, 'Third block')

    def testBlockchainHashIsAccurate(self):
        blockchain = Blockchain()
        blockchain.addBlock('First block')
        blockchain.addBlock('Second block')
        blockchain.addBlock('Third block')
        self.assertEqual(
            blockchain.last_hash, blockchain.blocks.next.next.hash)


if __name__ == "__main__":
    unittest.main()
