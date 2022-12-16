class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(a,b)
    def sum(self,x,y):
        return x*y

test_class = test(100,5)
test_class.a = 200
print(test_class.sum(test_class.a,test_class.b))