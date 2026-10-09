A=int(input())
B=int(input())
S=int(input())

if(A!=0 and A!=1)or(B!=0 and B!=1):
    print("輸入錯誤")
else:
    if A!=B:   #如果A、B只有一個按鈕被按下
        middle=1  
    else:
        middle=0    

    if middle==1 and S==1: #如果A、B恰好一個按鈕被按下、且安全開關已開啟
        start=1  #允許啟動
    else:
        start=0  #不允許啟動
    

    print(f'第一個閘輸出={middle}')
    print(f'允許啟動={start}')
 