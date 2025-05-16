class Solution:
    def nthFibonacci(self, n: int) -> int:
        if(n<=1):
            return n
        return self.f(n-1)+self.(n-2)
        