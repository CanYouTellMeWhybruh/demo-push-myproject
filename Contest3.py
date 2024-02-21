# from math import *
# def prime(n):
#     if n<2: return False
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             return False
#     return True           
# n=int(input())
# if prime(n):
#     print('YES')
# else:
#     print('NO')
# for i in range(1,n+1):
#     if prime(i):
#         print(i,end=' ')
# KIEM TRA SO NGUYEN To VA LIET KE

# birth_day=int(input('nhap ngay sinh cua ban: '))
# birth_month=int(input('nhap thang sinh cua ban :'))
# birth_year=int(input('nhap nam sinh cua ban: '))

# current_day=int(input('hom nay ngay may: '))
# current_month=int(input('bay gio la thang may: '))
# current_year=int(input('bay gio la nam bao nhieu: '))
# day_aged=0
# month_aged=0
# year_aged=0
# if (current_month - birth_month) < 0:
#     year_aged=current_year - birth_year - 1
#     month_aged=12-(birth_month-current_month)
#     day_aged=current_day-birth_day
# else:
#     year_aged=current_year - birth_year
#     month_aged=current_month-birth_month
#     day_aged=current_day-birth_day
# print("tuoi cua ban la: ",'%d tuoi' %(year_aged) ,'%d thang '%(month_aged),'%d ngay'%(day_aged))
