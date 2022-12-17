class test:
    def __init__(self,a: int,b = 0):
        assert a >= 0,f"a {a} must greater than or equal to zero"
        assert b >= 0,f"b {b} must greater than or equal to zero"
        self.a = a
        self.b = b
        print(a,b)
    def sum(self):
        return self.a * self.b

test_class = test(100,-5)
test_class_2 = test(1100)
test_class.a = 200
print(test_class.sum())
print(test_class_2.sum())