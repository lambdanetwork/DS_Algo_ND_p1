from LinkedList import LinkedList


def union(llist_1, llist_2):
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


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
