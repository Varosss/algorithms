# 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def reverseList(self, head):
        list = []
        List = head
        while List:
            list.append(List.val)
            List = List.next

        List = head

        for i in range(len(list) - 1, -1, -1):
            List.val = list[i]
            List = List.next

        return head


def createLinkedList(list):
    List = ListNode()
    head = List
    for i in range(len(list)):
        List.val = list[i]
        if i < len(list) - 1:
            List.next = ListNode()
            List = List.next
    
    return head


def showLinkedList(head):
    while head:
        print(head.val)
        head = head.next

list = [1, 5, 6, 10, 324]

List = createLinkedList(list)
answer = Solution().reverseList(List)
showLinkedList(answer)