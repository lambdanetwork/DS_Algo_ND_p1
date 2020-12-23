
import sys
from Node import initNode, createOneNode, createNodesFromList, prettyPrintNode


def huffman_encoding(str):
    frequency_dict = {}

    for char in str:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    print(frequency_dict)

    def takeSecond(tuple):
        return tuple[1]
    ordered_list = [(k, v)
                    for k, v in frequency_dict.items()]
    ordered_list.sort(key=takeSecond)

    # 3.Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
    max_2 = ordered_list[-2:]
    max_node = createOneNode(max_2[0], max_2[1])
    rest = ordered_list[0:-2]
    rest_node = createNodesFromList(rest)

    # 4.combine rest_node and max_node
    final_node = createOneNode(rest_node, max_node)
    print('final_node', final_node)

    # 5. traverse from root


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
