# 2. Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, list1, list2):
        if not list1 and not list2:
            return None

        def getInt(list):
            degree = 0
            num = 0
            while list:
                num += list.val * (10 ** degree)
                list = list.next
                degree += 1
            
            return num


        def getList(num):
            list = []

            if num == 0:
                list.append(num)
                return list

            while num > 0:
                list.append(num % 10)
                num = num // 10
            
            return list


        def makeLinkedList(List):
            list = ListNode()
            head = list

            for i in range(len(List)):
                list.next = ListNode(List[i])
                list = list.next

            head = head.next 

            return head


        int1 = getInt(list1)
        int2 = getInt(list2)

        int3 = int1 + int2
        listPattern = getList(int3)

        list3 = makeLinkedList(listPattern)

        return list3       


def makeLinkedList(List):
    list = ListNode()
    head = list

    for i in range(len(List)):
        list.next = ListNode(List[i])
        list = list.next

    head = head.next 

    return head


list1 = makeLinkedList([0])
list2 = makeLinkedList([0])

list3 = Solution().addTwoNumbers(list1, list2)

while list3 is not None:
    print(list3.val)
    list3 = list3.next