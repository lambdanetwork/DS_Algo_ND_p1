
import sys
import unittest
from Node import createOneNode, createNodesFromList, encodeTree


def huffman_encoding(string):
    if type(string) != str or len(string) == 0:
        raise Exception("Provide String with length > 0")

    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    # ordering list
    def takeSecond(tuple):
        return tuple[1]
    ordered_list = [(k, v)
                    for k, v in frequency_dict.items()]
    ordered_list.sort(key=takeSecond)

    # edge case
    if len(ordered_list) == 1:
        char = ordered_list[0][0]
        frequency = frequency_dict[char]
        encodedString = ''
        for x in range(0, frequency):
            encodedString += '0'
        return (encodedString, {'left': ordered_list[0], 'value': '0'})

    FINAL_NODE = None
    if len(ordered_list) > 1 and len(ordered_list) <= 3:
        FINAL_NODE = createNodesFromList(ordered_list)
    else:
        # 3.Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
        max_2 = ordered_list[-2:]
        max_node = createOneNode(max_2[0], max_2[1])
        rest = ordered_list[0:-2]
        rest_node = createNodesFromList(rest)

        # 4.combine rest_node and max_node
        FINAL_NODE = createOneNode(rest_node, max_node)

    # 5. traverse from root
    dict_char_code = encodeTree(FINAL_NODE)
    encoded_string = ''
    for char in string:
        encoded_string += dict_char_code[char]
    return (encoded_string, FINAL_NODE)


def huffman_decoding(data, tree):
    if type(data) != str or len(data) == 0:
        raise Exception("Provide String with length > 0")
    if type(tree) != dict:
        raise TypeError("Provide a tree with Dict type")
    if len(data) == 1:
        return tree['value']

    decoded_string = ''
    current_node = tree

    def decodeByNode(char, node):
        if char == '0':
            if type(node['left']) == tuple:
                return node['left'][0]
            else:
                return node['left']
        else:
            if type(node['right']) == tuple:
                return node['right'][0]
            else:
                return node['right']

    for char in data:
        decoded = decodeByNode(char, current_node)
        if type(decoded) == dict:
            current_node = decoded
        else:
            # get the data, restart from tree
            decoded_string += decoded
            current_node = tree

    return decoded_string


# Unit test
class Testing(unittest.TestCase):

    def testSentence(self):
        a_great_sentence = "The bird is the word"
        encoded_data, tree = huffman_encoding(a_great_sentence)
        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

        self.assertEqual(decoded_data, a_great_sentence)

    def testVeryLongSentence(self):
        text = """“In the loveliest town of all, where the houses were white and high and the elms trees were green and higher than the houses, where the front yards were wide and pleasant and the back yards were bushy and worth finding out about, where the streets sloped down to the stream and the stream flowed quietly under the bridge, where the lawns ended in orchards and the orchards ended in fields and the fields ended in pastures and the pastures climbed the hill and disappeared over the top toward the wonderful wide sky, in this loveliest of all towns Stuart stopped to get a drink of sarsaparilla.”"""
        encoded_data, tree = huffman_encoding(text)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertEqual(decoded_data, text)

    def testEmptyString(self):
        data = ''
        with self.assertRaises(Exception):
            encoded_data, tree = huffman_encoding(data)

        with self.assertRaises(Exception):
            decoded_data = huffman_decoding(data, 'should be dict')

    def testRepeatedSingleCharacter(self):
        text = 'AAA'
        encoded_data, tree = huffman_encoding(text)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertEqual(decoded_data, text)

    def testRepeatedSingleCharacter(self):
        text = 'AAABBB'
        encoded_data, tree = huffman_encoding(text)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertEqual(decoded_data, text)

    def testRepeatedSingleCharacter(self):
        text = 'AAABBBCCC'
        encoded_data, tree = huffman_encoding(text)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertEqual(decoded_data, text)


if __name__ == "__main__":
    unittest.main()
