i=1
M=int(input("ระยะทาง"))
while M >0:
    if(i==1):
        M=M-12
        print("วันที่",i,"เหลือระยะทาง",M,"1")
        i=i+1
    elif ( i%3==0):
        M=M-0
        print("วันที่",i,"เหลือระยะทาง",M,"3")
        i=i+1
    elif(i%2!=0):
        M=M-12
        print("วันที่",i,"เหลือระยะทาง",M,"คี่")
        i=i+1
    elif( i%2==0):
        M=M-11
        print("วันที่",i,"เหลือระยะทาง",M,"คู่")
        i=i+1
print("อูฐไปถึงที่ภายใน",i-1,"วัน")