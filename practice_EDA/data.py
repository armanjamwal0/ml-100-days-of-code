def fact(a):
    ans = 1
    for a in range(1,a+1):
        ans *= a
    return ans 
print(fact(5))