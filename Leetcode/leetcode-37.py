# 141. Linked List Cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        links = set()
        List = head

        while List:
            if List not in links:
                links.add(List)
                List = List.next
            else:
                return True

        return False


def createLinkedList(list):
    List = ListNode(0)
    head = List
    for i in range(len(list)):
        List.val = list[i]
        if i < len(list) - 1:
            List.next = ListNode(0)
            List = List.next
    
    tail = List

    return head, tail


def showLinkedList(head):
    while head:
        print(head.val)
        head = head.next

list = [1, 4, 6]
head, tail = createLinkedList(list)

print(Solution().hasCycle(head))