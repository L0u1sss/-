i=0
M=int(input("ระยะทาง"))
while (True):
    if (M>0):
        i=i+1
        M=M-3
        if (M<=0):
            break
        print("ระยะทางเหลือ",M,"เช้าวันที่",i)
        if (M<=0):
            break
        M=M+2
        print("ระยะทางเหลือ",M,"คืนวันที่",i)
print("หอยทากใช้เวลา",i,"วันในการเดินถึงปากบ่อ")