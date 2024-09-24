# #Activity1
# def function(n):
#     return n*(n+1)/2
# print(function(10))

#Activity2
#def function2(n):
#    sum=0
#    for i in range (1,n+1):
 #       sum+=i
 #   return sum
#print(function2(10))
#Activity3
def function3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
print(function3(10))