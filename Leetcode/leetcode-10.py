# 67. Add Binary

class Solution:
    def addBinary(self, a, b):
        def reverseString(string):
            newStr = ''
            for i in range(len(string) - 1, -1, -1):
                newStr += string[i]

            return newStr

        def addZero(point, string):
            newString = ''
            while len(newString + string) != point:
                newString += '0'

            newString += string

            return newString

        N = max(len(a), len(b)) + 1
        a = addZero(N, a)
        b = addZero(N, b)

        answer = ''
        rank = 0

        for i in range(N - 1, -1, -1):
            if a[i] != b[i]:
                if rank > 0:
                    answer += '0'
                else:
                    answer += '1'

            elif a[i] == b[i] == '0':
                if rank > 0:
                    answer += '1'
                    rank = 0
                else:
                    answer += '0'

            elif a[i] == b[i] == '1':
                if rank == 0:
                    answer += '0'
                    rank = 1
                else:
                    answer += '1'
        
        answer = reverseString(answer)
        if answer[0] == '0':
            answer = answer[1:]

        return answer

print(Solution().addBinary('1010', '1011'))