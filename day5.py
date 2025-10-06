oops concept

class person:
   def __init__(self,name,age):
       self.name = name
       self.age = age
    
   def __str__(self):
    return f"{self.name},{self.age} years old"
        
person= person("Raji",27)
print(person)

class dog:
   def __init__(self,name,age):
       self.name = name
       self.age = age
    
   def __str__(self):
    return f"{self.name},{self.age} years old "
        
dog= dog("chintu",1)
print(dog)
