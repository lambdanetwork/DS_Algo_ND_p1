class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left  # could be tuple or Node
        self.right = right  # could be tuple or Node


def createOneNode(left, right):
    total_value = 0

    if type(left) == tuple:
        total_value += left[1]
    else:
        total_value += left.value

    if type(right) == tuple:
        total_value += right[1]
    else:
        total_value += right.value

    node = Node(total_value, left, right)
    return node


def createNodesFromList(array):
    first = array[0]
    second = array[1]
    rest = array[2:]
    genesis_node = createOneNode(first, second)
    return recursiveCreateNode(genesis_node, rest)


def recursiveCreateNode(node, arr):
    if len(arr) == 0:
        return node

    tupl = arr.pop(0)
    new_node = createOneNode(node, tupl)
    return recursiveCreateNode(new_node, arr)
