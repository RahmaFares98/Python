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
print(n)	# should print 5
# run each of the methods a few more times and check the result!
x = md.add(10,9,3,4,2,1).result
y=md.add(2).add(5,6,3,7,2).subtract(3,5,1,8,3).add(100).result
print(x)
print(y)
y=md.add(4).subtract(4,2).result
print(y)


