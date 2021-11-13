#to run C:\Users\Rohan\Desktop\Python Programs>python3 calculator.py
#class has all functions which are instantiated by the object r of type calculator. self variable is req everywhere as every function call invisibly passes
# the object reference as a parameter.
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def menu(self):
        print("Menu\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
r=Calculator()
count=1
while count ==1:
    r.menu()
    c=int(input("Enter Choice:"))
    if c==1:
        a=int(input("Enter Number1:"))
        b=int(input("Enter Number2:"))
        print("Sum is ", r.add(a,b))
    if c==2:
        a=int(input("Enter Number1:"))
        b=int(input("Enter Number2:"))
        print("Subtraction is ", r.sub(a,b))
    if c==3:
        a=int(input("Enter Number1:"))
        b=int(input("Enter Number2:"))
        print("Multiplication is ", r.mul(a,b))
    if c==4:
        a=int(input("Enter Number1:"))
        b=int(input("Enter Number2:"))
        print("Division is ", r.div(a,b))
    elif c==5:
        print("Bye-bye")
        exit()
    else:
        continue
        
    
    
    

