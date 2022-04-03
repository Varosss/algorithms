# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None

        mergedList = ListNode()
        head = mergedList
        
        while list1 and list2:
            if list1.val <= list2.val:
                mergedList.next = ListNode(list1.val)
                list1 = list1.next

            else:
                mergedList.next = ListNode(list2.val)
                list2 = list2.next

            mergedList = mergedList.next

        while list1 is not None:
            mergedList.next = ListNode(list1.val)
            list1 = list1.next
            mergedList = mergedList.next

        while list2 is not None:
            mergedList.next = ListNode(list2.val)
            list2 = list2.next
            mergedList = mergedList.next

        return head.next


def makeLinkedList(List):
    list = ListNode()
    head = list

    for i in range(len(List)):
        list.next = ListNode(List[i])
        list = list.next

    head = head.next 

    return head

list1 = makeLinkedList([1, 2, 4, 7, 10, 27, 29])
list2 = makeLinkedList([3, 8, 10, 19, 28, 34, 78])

print(list1.val, list2.val)

list3 = Solution().mergeTwoLists(list1, list2)

while list3 is not None:
    print(list3.val)
    list3 = list3.next