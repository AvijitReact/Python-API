def hello(name='Jose'):
    print('Hello Function has been Run') 
    
    def greet():
        return "within greet"
     
    print(greet())
    
hello()
#greet()

def hello_world():
  name = str(input("Enter your name: "))
  if name == 'AV':
    ret = "Hello " + str(name)
  else:
    ret = "My World"
  return ret
  
ret1 = hello_world()
print (ret1)