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

def plus(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum  
print(plus(20,30,40,50))

#fibbonacchi Number

input = 5

list = [1,1,2,3,5]

fib = map((lambda X: X * X * X), list)

print(fib)