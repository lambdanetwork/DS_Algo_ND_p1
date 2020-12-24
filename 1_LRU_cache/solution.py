import unittest

# double linkedlist


class Node:
    def __init__(self, key, value):
        # store key and value, so we can remove from data::Dict
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise Exception("Provide a value bigger than 0")
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.data = {}

    def log(self):
        print('head = ', self.head.key, self.head.value)
        print('tail = ', self.tail.key, self.tail.value)

    def remove(self, key):
        # get node
        node = self.data[key]
        self.data.pop(key)
        self.size -= 1

        # remove prev of node
        if node.prev != None:
            node.prev.next = node.next
        else:
            # if this is the first node (without prev)
            self.head = node.next

        # remove next of node
        if node.next != None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = -1
        try:
            value = self.data[key].value
        except:
            return value

        # if found, remove the key from it's position, and move it to self.head, by using self.set
        self.remove(key)
        self.set(key, value)
        return value

    def set(self, key, value):
        if key == None or value == None:
            raise Exception('value cannot be null')

        # check capacity and remove last element
        if self.size == self.capacity:
            self.remove(self.tail.key)

        node = Node(key, value)
        self.size += 1

        # if first node
        if self.head == None:
            self.head = self.tail = node
        else:
            # always add to head of LRU, to make it recent
            self.head.prev = node
            self.head = node
        self.data[key] = self.head


class Testing(unittest.TestCase):
    def testWithCapacity0(self):
        with self.assertRaises(Exception):
            our_cache = LRU_Cache(0)

    def testOrderOfQueue(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        self.assertEqual(our_cache.head.value, 4)
        self.assertEqual(our_cache.tail.value, 1)

    def testGetValue(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        answer1 = our_cache.get(1)       # returns 1
        asswer2 = our_cache.get(2)       # returns 2
        self.assertEqual(answer1, 1)
        self.assertEqual(asswer2, 2)

        # 2 becomes the head, while 3 becomes the tail
        self.assertEqual(our_cache.head.value, 2)
        self.assertEqual(our_cache.tail.value, 3)

    def testNotFoundValue(self):
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)

        answer = our_cache.get(9)
        self.assertEqual(answer, -1)

    def testMaxCapacity(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        our_cache.set(5, 5)
        our_cache.set(6, 6)
        self.assertEqual(our_cache.capacity, 5)


if __name__ == "__main__":
    unittest.main()
