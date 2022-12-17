class test:
    rate = 0.8
    all = []
    def __init__(self,name:str,a: int,b = 0):
        assert a >= 0,f"a {a} must greater than or equal to zero"
        assert b >= 0,f"b {b} must greater than or equal to zero"
        self.name = name
        self.a = a
        self.b = b
        self.all.append(self)

    def sum(self):
        return self.a * self.b

    def apply_discount(self):
        self.a  *= self.rate

    def __repr__(self):
        return f"test:{self.name}"

test_class = test("earphone",100,5)
test_class_2 = test("PC",1000,5)
test_class.rate = 2
test_class.apply_discount()

for i in test.all:
    print(i.__repr__())
    print(i.sum())