flower=[]

for i in range(1,1001):
    flower.append(i)
    print(flower[i-1])
for i in range(1,1000):
 print(i)

for i in range(1,6):
    print(i)
    
j=1
while(j<6):
    print(j)
    j+=1
    
k=1
while k<51:
    print(k)
    k+=2
    
n=int(input("Enter a number"))
if n%2==0:
    print("It is an even number")
else:
    print("it is an odd number")

list=[1,2,3,3,4,5,5]
k=set(list)
print(k)
k.add(6)
print(k)

dict={
    "model":"1st model",
    "year":2021
}
print(type(dict))
print(dict)

dict={
    "model":"2nd model",
    "year":2022,
    "age":27
}
print(type(dict))
print(dict['model'])
dict['city']='hyderabad'
print(dict)

def mom(a,b):
    print(a+b)
    
a=10
b=20
mom(a,b)
mom(5,6)
mom(a,b)
mom(5,6)
