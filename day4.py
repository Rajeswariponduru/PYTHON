list=[1,2,3,4,5,6,7,8,9]
print(list[4:8])

list=[1,2,3,4,5,6,7,8,9]
print(list[4:9])

list=[1,2,3,4,5,6,7,8,9]
print(list[4:])

list=[1,2,3,4,5,6,7,8,9]
print(list[1::2])

list=[1,2,3,4,5,6,7,8,9]
print(list[0::3])

functions

def mom(a,b):
    print(a+b)
    
a=10
b=20
c=mom(a,b)
print(c

      def mom(a,b):
    return(a+b)
    
a=10
b=20
c=mom(a,b)
print(c)

end

if True:
    print("valid")
else:
    print("invalid")

end

exceptions

try:
    a= int(input("Enter first number"))
    b= int(input("Enter second number"))
    result = a+b
    print("sum:",result)
except ValueError:
    print("Invalid input! please enter numbers only.")
    
    
try:
    a= int(input("Enter first number"))
    b= int(input("Enter second number"))
    result = a+b
    print("sum:",result)
except ValueError:
    print("Indentation error")

try:
    num = int(input("Enter first number"))
    result = 10 / num
    print("Result:",result)
except ValueError:
    print("Invalid input! please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("An error occured:",e)
finally:
    print("Execution Finished")
    
    
