from LinkedList import LinkedList
import unittest


def checkListSizes(llist_1, llist_2):
    answer_llist = LinkedList()
    llist1_size = llist_1.size()
    llist2_size = llist_2.size()
    if llist1_size == 0 and llist2_size == 0:
        return answer_llist
    elif llist1_size == 0 and llist2_size > 0:
        return llist_2
    elif llist1_size > 0 and llist2_size == 0:
        return llist_1
    else:
        return None


def union(llist_1, llist_2):
    if not isinstance(llist_1, LinkedList) or not isinstance(llist_2, LinkedList):
        raise Exception("Provide both LinkedList object")

    checkSize = checkListSizes(llist_1, llist_2)
    if checkSize != None:
        return checkSize

    # store the value in dictionary and later we will create a linkedlist based on the dictionary
    answer = {}
    answer_llist = LinkedList()

    def populateAnswer(node):

        if not node.value in answer:
            answer[node.value] = True
            answer_llist.append(node.value)

        if(node.next != None):
            populateAnswer(node.next)

    populateAnswer(llist_1.head)
    populateAnswer(llist_2.head)

    return answer_llist


def intersection(llist_1, llist_2):
    if not isinstance(llist_1, LinkedList) or not isinstance(llist_2, LinkedList):
        raise Exception("Provide both LinkedList object")

    checkSize = checkListSizes(llist_1, llist_2)
    if checkSize != None:
        return checkSize

    # store the value in dictionary and later we will create a linkedlist based on the dictionary
    list1 = {}
    answer_llist = LinkedList()

    def populatelist1(node):
        list1[node.value] = True
        if(node.next != None):
            populatelist1(node.next)

    def checklist2(node):
        if(node.value in list1):
            answer_llist.append(node.value)
        if(node.next != None):
            checklist2(node.next)

    populatelist1(llist_1.head)
    checklist2(llist_2.head)

    return answer_llist


# Unit test
class Testing(unittest.TestCase):
    def testCase1(self):
        # Test case 1
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        answer = union(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), 11)
        answer = intersection(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), 4)

    def testCase2(self):
        # Test case 2
        linked_list_3 = LinkedList()
        linked_list_4 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]

        for i in element_1:
            linked_list_3.append(i)

        for i in element_2:
            linked_list_4.append(i)

        answer = union(linked_list_3, linked_list_4)
        self.assertEqual(answer.size(), 13)
        answer = intersection(linked_list_3, linked_list_4)
        self.assertEqual(answer.size(), 0)

    def testEmptyList(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        answer = union(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), 0)
        answer = intersection(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), 0)

    def testOneEmptyList(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        for i in element_1:
            linked_list_1.append(i)

        answer = union(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), len(element_1))
        answer = intersection(linked_list_1, linked_list_2)
        self.assertEqual(answer.size(), len(element_1))


if __name__ == "__main__":
    unittest.main()
