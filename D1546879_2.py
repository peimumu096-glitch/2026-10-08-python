A = int(input())
B = int(input())

if(A!=0 and A!=1)or(B!=0 and B!=1):
    print("輸入錯誤")
else:
    if A==1 or B==1:
        a1=1
    else:
        a1=0

    if A==1 and B==1:
        a2=1
    else:
        a2=0

    if A!=B:
        a3=1
    else:
        a3=0

    print('OR=',a1)
    print('AND=',a2)
    print('XOR=',a3)