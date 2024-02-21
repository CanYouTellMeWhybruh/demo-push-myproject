# n=int(input())
# if n<0:
#     print('NO')
# elif n<=2:
#     print('NO')
# else:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print('NO')
#             break
#     else:
#         print("YES")
# from math import *
# n=int(input())
# if n==1 and n==3:
#     print(-1)
# elif n%2==0:
#     print(n//2)
#     for i in range(1,n//2+1):
#         print(2,end=' ')
# else:
#     print(n//2)
#     for i in range(1,n//2):
#         print(2,end=' ')
#     print(3)
from math import *
# n=int(input())
# if n<2:
#     print('NO')
# elif n<0:
#     print("NO")
# else:
#     for i in range(2,isqrt(n)+ 1):
#         if n%i==0:
#             print('NO')
#             break
#     else:
#         print("YES")       
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        if j<i:
            print(' ',end='')
        else:
            print('*',end='')
    print('')