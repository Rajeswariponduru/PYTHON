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

def mom(a,b):
    print(a+b)
    
a=10
b=20
c=mom(a,b)
print(c)
d=mom(5,6)
print(d)
e=mom(a,b)
print(e)
f=mom(5,6)
print(f)
