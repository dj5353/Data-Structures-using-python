'''
#This is the fastest WAY to solve a fibonacci sequence with O(1) time complexity and O(1) space complexity
#Golden ratio = int((1+5**0.5)/2) ~ 1.61803
def fibonacci(n):
    golden_ratio = (1+5**0.5)/2
    return int((golden_ratio ** n +1)/5**0.5)
print(fibonacci(1045))

'''
def fibonacci(n):
    golden_ratio = (1+5**0.5)/2
    return int((golden_ratio**n + 1)/5**0.5)
print(fibonacci(4-1))


''' To get the fibonacii upto '''
def fibo_calc(nums):
    list = []
    for i in range(nums):
        gloden_ratio = (1 + (5**0.5))/2
        print(int((gloden_ratio**i + 1)/5**0.5))
fibo_calc(7)
gloden_ratio = (1 + (5**0.5))/2
print([int((gloden_ratio**i + 1)/5**0.5) for i in range(0,6)])

