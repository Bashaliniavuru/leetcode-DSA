class Solution:
    def compute(self,a,b,operator):
        if operator=="+":
            return a+b
        if operator=='-':
            return a-b
        if operator=="*":
            return a*b
        if operator=="/":
            return int(a/b)
    def evalRPN(self,tokens)->int:
        stack=[]
        for token in tokens:
            if token in "+-*/":
                b=stack.pop()
                a=stack.pop()
                res=self.compute(a,b,token)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]

        