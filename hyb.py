# Base Class #
class A:
   def m1(self):
      print("Method m1 from class A")

# Hierarchical inheritance #
class B(A):
    def m2(self):
        print("Method m2 from class B")

class C(A):
    def m3(self):
        print("Method m3 from class C")

class D:
    def m4(self):
        print("Method m4 from class D")

# Multilevel inheritance #
class E(B):
    def m5(self):
        print("Method m5 from class E")

# multiple Inheritance #
class F(C,D):
    def m6(self):
        print("Method m6 from class F")

## object of class E ##
jay = E()
print("By using object jay of class E:")
jay.m1()
jay.m2()
jay.m5()

## object of class F ##
viru = F()
print("By using object viru of class F: ")
viru.m1()
viru.m3()
viru.m4()
viru.m6()
