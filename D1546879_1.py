n=int(input("請輸入數字"))
if n>=0 and n<=15:
    t1=n//8
    t12=n%8
    t2=t12//4
    t22=t12%4
    t3=t22//2
    t32=t22%2
    t4=t32//1
    t42=t32%1

else:
    print('輸入錯誤')

print('二進制=',t1,t2,t3,t4)

if n>=0 and n<=15:
    e=n//8
    e1=n%8
    print('八進制=',e,e1)
else:
    print('輸入錯誤')
    
if n < 10:
    s = n
elif n==10:
    s="A"
elif n==11:
    s="B"
elif n==12:
    s="C"
elif n==13:
    s="D"
elif n==14:
    s="E"
elif n==15:
    s="F"
print('十六進制=',s)