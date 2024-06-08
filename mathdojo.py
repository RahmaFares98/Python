class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for n in nums:
            self.result+=n
        return self
    def subtract(self, num, *nums):
        self.num=num
        self.result-=num
        for n in nums:
            self.result-=n
        return self
    
# create an instance:
md = MathDojo()
# to test:
n = md.add(2).add(2,5,1).subtract(3,2).result
print(f"the value of y is equal {n}")# should print 5
# run each of the methods a few more times and check the result!
x = md.add(10,9,3,4,2,1).result
y=md.add(2).add(5,6,3,7,2).subtract(3,5,1,8,3).add(100).result
y=md.add(4).subtract(4,2).result
y=md.add(10).result         
y=md.subtract(5).result
print(f"the value of y is equal {y}")
x=md.add(3, 4, 5).add(4,3).add(4,5,2,7,1).result    
x=md.subtract(1, 1, 1).subtract(1,4).subtract(3).result
print(f"the value of x is equal {x}")
