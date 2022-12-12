# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python ?


class Calculation1:  

    def Summation(self,a,b):  

        return a+b;  

class Calculation2:  

    def Multiplication(self,a,b):  

        return a*b;  

class Derived(Calculation1,Calculation2):  

    def Divide(self,a,b):  

        return a/b;  

d = Derived()  

print(d.Summation(10,20))  

print(d.Multiplication(10,20))  

print(d.Divide(10,20))