# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def listToInt(node):
            currentNode = node
            listStr = str(node.val)
            while currentNode.next is not None:
                currentNode = currentNode.next
                listStr = str(currentNode.val) + listStr  # expensive !
            return int(listStr)

        result = listToInt(l1) + listToInt(l2)
        result = str(result)[::-1]
        resultList = ListNode(result[0])
        currentNode = resultList
        for i in result[1:]:
            node = ListNode(i)
            currentNode.next = node
            currentNode = node

        return resultList
