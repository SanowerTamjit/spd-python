def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def math_ops(x, y):
    result = [sum(x,y) , sub(x,y), mult(x,y), x/y]
    return result

# 10  1*2*3*4*5*6*&*8*9*10
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

# 10 * fact(9) = 
#         9 * fact(8)= 
#             8 * fact(7) = 
#                 7 * fact(6) = 
#                     6 * fact(5) =
#                         5 * fact(4) = 
#                             4 * fact(3) = 24
#                                 3 * fact(2) = 6 
#                                     2 * fact(1) = 2
#                                         1


division = lambda x,y : print (x/y)

values = math_ops(20,2)
print(values[3])
division(30,2)
print(fact(10))