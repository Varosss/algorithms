# 160. Intersection of Two Linked Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        links = set()

        ListA = headA

        while ListA:
            links.add(ListA)
            ListA = ListA.next

        while headB:
            if headB in links:
                return headB.val

            headB = headB.next
        
        return None


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


patternA = [4, 1]
patternB = [5, 6, 1]
patternC = [8, 4, 5]

headA, tailA = createLinkedList(patternA)
headB, tailB = createLinkedList(patternB)
headC, tailC = createLinkedList(patternC)

tailA.next = headC
tailB.next = headC

# tailA = tailA.next
# tailB = tailB.next
# print(tailA.val, tailB.val)

print(Solution().getIntersectionNode(headA, headB))