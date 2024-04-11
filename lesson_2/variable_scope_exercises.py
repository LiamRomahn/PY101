#1
# num = 5

# def my_func():
#     print(num)

# my_func() #it will print 5

#2
# num = 5

# def my_func():
#     num = 10

# my_func()
# print(num) #it will print 5

#3
# num = 5

# def my_func():
#     global num
#     num = 10

# my_func()
# print(num) #it will print 10

#4
# def outer():
#     outer_var = 'Hello'

#     def inner():
#         inner_var = 'World'
#         print(outer_var, inner_var)

#     inner()

# outer()

#5
# def my_func():
#     num = 10

# my_func()
# print(num)

#6
# def my_func():
#     x = 15

#     def inner_func1():
#         x = 25
#         print("Inner 1:", x)

#     def inner_func2():
#         print("Inner 2:", x)

#     inner_func1()
#     inner_func2()

# my_func() #print 25 \n 15