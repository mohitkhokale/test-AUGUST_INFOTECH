# 2) Explain overloading and overriding by writing a sample program. [2.5 marks]

# overloading example 

def product(a,b):
    p = a*b
    print(p)

def product(a,b,c):
    p = a*b*c
    print(p)


product(2,4,8)


# overriding

class C1:
    def test(self):
        print("Hi C1 class")

class C2:
    def test(self):
        print("Hi C2")

c1 = C1()
c2 = C2()

c1.test()
c2.test()