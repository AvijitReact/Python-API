from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)

X = lambda Y: Y + 10
print(X(12))

X = lambda M, N: M * N
print(X(2,4))

X = lambda M: M if M > 10 else "XX"
print(X(9))

#introduction to Filter
my_list = [12,23,4]
result = list(filter(lambda x: (x % 2 == 0), my_list))           
print(result)

my_list = [12,'XX',24]
result = list(filter(lambda X:(isinstance(X, int)), my_list))
print(result)

li = [1,2,3,4,5]
res = list(map(lambda x: (x + 5), li))
sum = reduce((lambda X, Y: (X + Y)), res) 
print(sum)
#x =10
#print(type(my_list(1)))

input = 5
list1 = [1,1,2,3,5]
fib = list(map(lambda X: (X * X * X), list1))
print(fib)