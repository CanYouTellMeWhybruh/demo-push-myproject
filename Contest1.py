# a,b,c=map(int,input().split())
# if a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c>a):
#     if a==b==c:
#         print('1')
#     elif (a==b!=c) or (a==c!=b) or (b==c!=a):
#         print("2")
#     elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#         print('3')
#     else:
#         print('4')
# else:
#     print('INVALID')
#    KIEM TRA TAM GIAC
# t,n=map(int,input().split())
# if n > 0 and (t>=1 and t<=12):
#     if n%400==0 or (n%4==0 and n%100!=0) :
#         if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
#             print('31')
#         elif t==2:
#             print('29')
#         elif t==4 or t==6 or t==9 or t==11:
#             print('30')
#     else:
#         if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
#             print('31')
#         elif t==2:
#             print('28')
#         elif t==4 or t==6 or t==9 or t==11:
#             print('30')
# else:
#     print("INVALID")
#    KIEM TRA NGAY THANG
# n=int(input())
# nam=n//365
# tuan=(n-365)//7
# ngay=(n-365)%7
# print(nam,tuan,ngay,sep=' ')
# DOI NGAY SANG NAM TUAN NGAY
# x,y,z,t=map(float,input().split())
# total=((x+y)+(z*2)+(t*3))/7
# if total >= 8:
#     print('GIOI')
# elif total < 8 and total >=6.5 :
#     print('KHA')
# elif total <6.5 and total >=5:
#     print('TRUNG BINH')
# elif total >=0 and total <5:
#     print("YEU")
# DANH GIA HOC SINH
# n,a,b=map(int,input().split())
# if n%2==0:
#     if a>=(b/2):
#         print((n//2)*b)
#     else:
#         print((n*a))
# else:
#     if a>=(b/2):
#         print(((n//2)*b)+a)
#     else:
#         print(n*a)
# MUA NUOC
# tu A --> Z ma ascii la tu 65 --> 90
# tu a --> z ma ascii la tu 97 --> 122
# tu 0-->9 la 48--57
# c=input()
# if c == 'z' or c == 'Z':
#     print('a')
# else:
#     g=ord(c)
#     g+=1
#     print(chr(g).lower())
# VIET KI TU KE TIEP
# c=input()

# if ord(c) >= 65 and ord(c) <= 90:
#     print("UPPER")
# elif ord(c) >= 97 and ord(c) <= 122:
#     print('LOWER')
# elif ord(c) >= 48 and ord(c) <= 57: 
#     print('DIGIT')
# else:
#     print('SPECIAl')
# c=input()
# if c.islower():
#     print('LOWER')
# elif c.isupper():
#     print('UPPER')
# elif c.isdigit():
#     print('DIGIT')
# else:
#     print("SPECIAL")
# KIEM TRA KI TU
# c=input()
# if c.isupper():
#     print(chr(ord(c)).lower())
# elif c.islower():
#     print(chr(ord(c)).upper())
# else:
#     print(c)
# CHUYEN DOI CHU 
# m,n=map(int,input().split())
# if (m*n)%2==0:
#     print((m*n)//2)
# else:
#     print((m*n)//2)
# DOMINO
# n,m,a=map(int,input().split())
# if m%a==0 and n%a==0:
#     print((m//a)*(n//a))
# elif m%a==0 and n%a!=0:
#     print((m//a)*((n//a)+1))
# elif m%a!=0 and n%a==0:
#     print(((m//a)+1)*(n//a))
# else:
#     print(((m//a)+1)*((n//a)+1))
# LAT DA QUANG TRUONG
# a,b,k=map(int,input().split())
# if k%2==0:
#     print(a*(k//2)-b*(k//2))
# else:
#     print(a*((k//2)+1)-b*(k//2))
# FROG
# n,s=map(int,input().split())
# if s%n==0:
#     print(s//n)
# else:
#     print((s//n)+1)
# DONG XU
# n,m=map(int,input().split())
# min,max=0,n
# if n%2==0:
#     min=n//2
# else:
#     min=(n//2)+1
# ans=(min+m-1)//2 *m
# if ans<max:
#     print(ans)
# else:
#     print(-1)
# DOREMON
# from math import *
# d1,d2,d3=map(int,input().split())
# c1=(d1+d3)*2
# c2=(d2+d3)*2
# c3=d1+d2+d3
# c4=(d1+d2)*2
# print(min(c1,c2,c3,c4))
# TIM QUANG DUONG NGAN NHAT
# n=int(input())  C1
# if n%100==0:
#     print(n//100)
# else:
#     if (n%100)%20==0:
#         print((n//100)+(n%100)//20)
#     else:
#         if ((n%100)%20)%10==0:
#             print((n//100)+(n%100)//20+((n%100)%20)//10)
#         else:
#             if (((n%100)%20)%10)%5==0:
#                 print((n//100)+(n%100)//20+((n%100)%20)//10+(((n%100)%20)%10)//5)
#             else:
#                 print((n//100)+(n%100)//20+((n%100)%20)//10+(((n%100)%20)%10)//5+((((n%100)%20)%10)%5)//1)
# C2
# n=int(input())
# ans=n//100
# n%=100
# ans+=n//20
# n%=20
# ans+=n//10
# n%=10
# ans+=n//5
# n%=5
# ans+=n//1
# print(ans)
# DOI TIEN
# n,u1,d=map(int,input().split())
# print((n*u1)+(n*d*(n-1)//2))
# CAP SO CONG
# a,b,c,d=map(int,input().split())
# if b%a==0 and b*(b//a)%c==0 and c*(b//a)%d==0:
#     print('YES')
# else:
#     print('NO')
# KIEM TRA CAP SO NHAN
# n=int(input())
# d=1
# u1=1
# n-=1
# print((n*u1)+(n*d*(n-1)//2))
# TO HOP CHAP
# a1,a2,a3,b1,b2,b3=map(int,input().split())
# n=int(input())
# total1=a1+a2+a3
# total2=b1+b2+b3
# if total1 % 5==0:
#     total1=total1//5
# else:
#     total1=(total1//5)+1
# if total2%10==0:
#     total2=total2//10
# else:
#     total2=(total2//10) +1
# if total1+ total2 <= n:
#     print('YES')
# else:
#     print('NO')
# BIZON THE CHAMPION
# from math import *
# k2,k3,k5,k6=map(int,input().split())
# k256=min(k2,k5,k6)
# k32=min(k3,k2-k256)
# print(256*k256+32*k32)
# GHEP SO
# a,b,c,n=map(int,input().split())
# du=(a+b+c+n)//3
# if (a+b+c+n)%3==0:
#     if du >= a and du >= b and du >=c:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
# CHIA TIEN
# c1,c2,c3,c4,c5=map(int,input().split())
# total=(c1+c2+c3+c4+c5)
# if total%5==0 and total!=0:
#     print(total//5)
# else:
#     print('-1')
#SU HAO PHONG
# h,m=map(int,input().split())
# conlai=24-h
# if h<24:
#     print((conlai*60)-m)
# elif conlai==24:
#     print('0')
# TINH SO GIO CON LAI TRUOC TET (HYPN)
# from math import *
# a,b,c=map(int,input().split())
# delta = b ** 2 - 4 * a * c
# x1=float((-b + sqrt(delta)) / (2 * a))
# x2=float((-b - sqrt(delta)) / (2 * a))
# if a==0:
#     if b==0:
#         if c==0:
#             print('VO SO NGHIEM')
#         else:
#             print('VO NGHIEM')
#     else:
#         if c==0:
#             print('{:.2f}'.format(0))
#         else:
#             print("{:.2f}".format(-c / b))
# else:
#     if delta < 0:
#         print('VO NGHIEM')
#     elif delta==0 :
#         print('{:.2f}'.format(-b / 2*a))
#     else:
#         print('{:.2f}'.format(x1),'{:.2f}'.format(x2))
# BAC HAI