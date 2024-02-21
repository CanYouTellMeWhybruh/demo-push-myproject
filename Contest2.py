# n=int(input())
# for i in range(1,n+1):
#     print(i,end=' ')
# print()
# for z in range(n,-1,-1):
#     print(z,end=' ')
# print()
# for i in range(0,n+1,2):
#         print(i,end=' ')
# print()
# for i in range(1,n+1,2):
#         print(i,end=' ')
# print()
# for i in range(0,n,4):
#         print(i,end=' ')
# print()
# for i in range(0,n):
#     print(chr(97+i),end=' ')
# print()
# for i in range(122-n+1,123):
#     print(chr(i),end=' ')
# VONG LAP
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+i
#     i+=1
# print(total)
# TINH TONG TU 1-->n
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+i**2
#     i+=1
# print(total)
# TINH TONG BINH PHUONG
# n=int(input())
# total=0
# for i in range(0,n+1):
#     if i%3==0:
#         total=total+i
# print(total)
# TONG CHIA HET CHO 3
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+(1/i)
#     i+=1
# print("{:.3f}".format(total))
# TONG NGHICH DAO  
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+(1/(2*i))
#     i+=1
# print("{:.5f}".format(total))
# TING TONG NHAN 2
# from math import *
# n=int(input())
# total1=0
# total2=0
# for i in range(1,isqrt(n)+1):
#     if n%i==0:
#         total1=total1+i
#         if i!=(n/i):
#             total2=total2+(n//i)
#         i+=1
# print(int(total1+total2))
# TONG CUA UOC
# from math import *
# n=int(input())
# dem=0
# for i in range(1,n+1):
#     if n%i==0:
#         dem+=1
#         i+=1
# print(dem)
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=' ')
#         i+=1
 # LIET KE UOC   
# from math import *
# n=int(input())
# for i in range(1,isqrt(n)+1):
#     print(i**2,end=' ')
# LIET KE SO CHINH PHUONG  
# from math import *
# n=int(input())
# tich=1
# tich2=1
# for i in range(1, isqrt(n)+1):
#     if n%i==0:
#         tich=tich*i
#         if n//i!=i:
#             tich=tich*(n//i)
# print(tich)
# TICH CUA UOC
# from math import *
# n=int(input())
# a=list(map(int,input().split()))
# if 2022 in a:
#     print('YES')
# else:
#     print('NO')
# KIEM TRA SO 2022
# n=int(input())
# total=0
# for i in range(1,n+1):
#     if i%2==0:
#         total=total+i
#     else:
#         total=total-i
# print(total)
# TONG CHAN LE
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+(i*2)
# print(total)
# TONG BOI 2
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+((i*2)-1)
# print(total)
# TONG LE
# n=int(input())
# total=0
# if n<=1000:
#     for i in range(1,n+1):
#         total=total+(i**3)
# print(total)
# TONG LAP PHUONG
# n=int(input())
# total=1
# if n<=15:
#     for i in range(1,n+1):
#         total=total*i
# print(total)
# TICH GIAI THUA
# n=int(input())
# count=0
# if n==0:
#     count=1
# else:
#     while n > 0:
#         n//=10
#         count+=1
# print(count)
# DEM SO LUONG CHU SO CUA N
# n=int(input())
# total=0
# if n==0:
#     total=0
# else:
#     while n>0:
#         total=total+(n%10)
#         n//=10
# print(total) 
# TONG CHU SO CUA    
# n=int(input())
# count=0
# while n>0:
#     if (n%10)<=1:
#         count=count+0
#     else:
#         for i in range(2,(n%10)//2+1):
#             if (n%10)%i==0:
#                 count+=0
#                 break
#         else:
#             count+=1
#     n//=10
# print(count)
# DEM SO NGUYEN TO CUA N (TINH CA SO 2)
# n=int(input())
# beer=n//28
# vo=beer
# while vo>=3:
#     count=vo//3
#     beer+=count
#     vo=vo%3+count
# print(beer)
# MUA BIA
# from math import *
# n=int(input())
# if n==1:
#     print(-1)
# elif n%2==0:
#     print(n//2)
#     for i in range(1,(n//2)+1):
#         print(2,end=' ')
# else:
#     print(n//2)
#     for i in range(1,n//2):
#         print(2,end=' ')
#     print(3)
# BIEU DIEN SO NGUYEN
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#     print('')
# print('')
# for i in range(n):
#     for j in range(n):
#             if i==0 or i==n-1 or j==0 or j == n-1:
#                 print('*',end='')
#             else:
#                 print('',end=' ')
#     print('')
# print('')
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end='')
#         else:
#             print('#',end='')
#     print('')
# print('')
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             end=print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print('')
#         VE HINH
# n=int(input())
# for i in range(n+1):
#     for j in range(i):
#         print('*',end='')
#     print('')
# print('')
# for i in range(n,-1,-1):
#     for j in range(i):
#         print('*',end='')  
#     print('')
# print('')
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j <= n-i:
#             print('',end=' ')
#         else:
#             print('*',end='')
#     print('')
# print('')
# for i in range(n,-1,-1):
#     for j in range(1,n+1):
#         if j<=n-i:
#             print('',end=' ')
#         else:
#             print('*',end='')
#     print('')
# print('')
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==i or i==n :
#             print('*',end='')
#         else:
#             print('',end=' ')
#     print(' ')
# VE HINH 2
# def hinh_1(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print('*',end='')
#         print('')
#     print('')
# def hinh_2(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print('*',end='')
#         print('')
#     print('')
# def hinh_3(n):
    
#     for i in range(n,0,-1):
#         for j in range(1,n+1):
#             if j<i:
#                 print(' ',end='')
#             else:
#                 print('*',end='')
#         print('')
#     print('')
# def hinh_4(n):
#     for i in range(0,n):
#         for j in range(1,n+1):
#             if j>i:
#                 print('*',end='')
#             else:
#                 print(' ',end='')
#         print('')
#     print('')
# def hinh_5(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if j==i or j==1 or i==n:
#                 print('*',end='')
#             else:
#                 print(' ',end='')
#         print('')
    
# n=int(input())
# hinh_1(n)
# hinh_2(n)
# hinh_3(n)
# hinh_4(n)
# hinh_5(n)
# SUA DOI BAI HINH 2
# def bruh(n):
#     a=1
#     b=n
#     for i in range(1,n+1):
#         for j in range(a,b+1):
#             print(j,end=' ')
#         print('')
#         a+=n
#         b+=n
#     print('')
# def bruh2(n):
#     a=1
#     b=n
#     for i in range(1,n+1):
#         for j in range(a,b+1):
#             print(j,end=' ')
#         print('')
#         a+=1
#         b+=1
#     print('')
# def bruh3(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if  j<=n-i:
#                 print('~',end='')
#             else:
#                 print(i,end='')
#         print('')
#     print('')
# def bruh4(n):
#     for i in range(1,n+1):
#         g=n-1
#         a=i
#         for j in range(i):
#             print(a,end=' ')
#             a=a+g
#             g-=1
#         print('')
#     print('')
# n=int(input())
# bruh(n)
# bruh2(n)
# bruh3(n)
# bruh4(n)
# def bruh(n):
#     gt=1
#     for i in range(1,n+1):
#         if n==1 or n==0:
#             gt=1
#         else:
#             gt*=i
#     return gt
# def bruh1(n):
#     gt2=1
#     for i in range(1,n+1):
#         if n==1 or n==0:
#             gt2=1
#         else:
#             gt2*=i
#     return gt2
# a,b=map(int,input().split())

# if a>b:
#     print(bruh(b))
# else:
#     print(bruh1(a))
# TIM UOC LON NHAT CUA 2 GT
# def gt(n):
#     tich=1 
#     for i in range(1,n+1):
#         tich*=i
#     return tich
# tong=1
# n=int(input())
# for i in range(1,n):
#     tong+=1/gt(i)
# print('{:.4f}'.format(tong))
# THUONG GIAI THUA
# a,b,n=map(int,input().split())
# check=False
# for i in range(0,n//a + 1):
#     temp=n-a*i
#     if temp%b==0:
#         check=True
#         break
# if check:
#     print('YES')
# else: 
#     print('NO')
# GIAI PHUONG TRINH
# n=int(input())
# while n>=10:
#     total=0
#     while n!=0:
#         total=total+n%10
#         n//=10
#     n=total
# print(n)
# DIGITAL ROOT
# def bruh(n):
#     gt=1
#     for i in range(1,n+1):
#         gt*=i
#     return gt
# def bruh2(n):
#     total=0
#     for i in range(1,n+1):
#         total+=bruh(i)
#     return total
# n=int(input())
# print(bruh2(n))
# TONG GIAi THUA
# n=int(input())
# g=list(map(int,input().split()))
# total=0
# for i in g:
#     if i%2==0:
#         total+=i
# print(total)
  # BAI 29
# t = int(input())
# for i in range(t):
#     n=int(input())
#     if n%2==0:
#         print("EVEN")
#     else:
#         print('ODD')
    # TEST CASE          
    







    
        
    
             
        
