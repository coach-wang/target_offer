class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return
        C = [1]
        for i in range(1, len(A)):
            C.append(C[i-1] * A[i-1])
        D = [1] * len(A)
        for i in range(len(A)-2, -1, -1):
            D[i] = D[i+1] * A[i+1]
        
        B = []
        for i in range(len(A)):
            B.append(C[i] * D[i])
        return B
