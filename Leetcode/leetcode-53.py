# 24. Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head:
            return 

        List = head
        count = 0
        prev = 0

        while List:
            if count % 2 == 0:
                prev = List.val

                if List.next:
                    List.val = List.next.val

                List = List.next

            else:
                List.val = prev
                List = List.next
                
            count += 1

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

list = [1, 2, 3, 4]
head = createLinkedList(list)

head = Solution().swapPairs(head)
showLinkedList(head)