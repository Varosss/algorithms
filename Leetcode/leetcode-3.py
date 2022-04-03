# 20. Valid Parentheses

class Solution:
    def isValid(self, s):

        def isOpeningBracket(bracket):
            if bracket == '(' or bracket == '[' or bracket == '{':
                return True

            return False


        def charsAreValid(char1, char2):
            if char1 == '(' and char2 == ')':
                return True
            
            if char1 == '[' and char2 == ']':
                return True
            
            if char1 == '{' and char2 == '}':
                return True

        if len(set(s)) == 1:
            s += ' '

        N = len(s)
        list = []
        last = -1

        try:
            for i in range(N):
                if isOpeningBracket(s[i]):
                    list.append(s[i])
                    last += 1

                elif charsAreValid(list[last], s[i]):
                    list.pop()
                    last -= 1

                else:
                    return False

        except IndexError:
            return False

        if list:
            return False
            
        return True

print(Solution().isValid("(})"))