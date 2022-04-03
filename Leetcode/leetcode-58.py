# 23. Merge k Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return

        nums = []

        def createLinkedList(list):
            List = ListNode()
            head = List
            for i in range(len(list)):
                List.val = list[i]
                if i < len(list) - 1:
                    List.next = ListNode()
                    List = List.next
            
            return head


        for i in range(len(lists)):
            while lists[i]:
                nums.append(lists[i].val)
                lists[i] = lists[i].next
        
        if not nums:
            return

        nums.sort()
        List = createLinkedList(nums)

        return List
    

def showLinkedList(head):
    while head:
        print(head.val)
        head = head.next


def createLinkedList(list):
    List = ListNode()
    head = List
    for i in range(len(list)):
        List.val = list[i]
        if i < len(list) - 1:
            List.next = ListNode()
            List = List.next

    return head


list1 = createLinkedList([0, 2, 5])
list2 = createLinkedList([1, 3, 4])
list3 = createLinkedList([2, 6])

list = [list1]

showLinkedList(Solution().mergeKLists(list))