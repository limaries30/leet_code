class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for t in s:
            if t==']':
                word = ''
                while stack[-1]!='[':
                    prev_word = stack.pop()
                    word = prev_word+word
                stack.pop() #'['제거1
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                for i in range(int(num)):
                    stack.append(word)
            else:
                stack.append(t)
        return ''.join(stack)