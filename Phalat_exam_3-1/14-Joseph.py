i=int(input("เลข"))
sur= ["A","B","C","D","E","F","G","H","I","J","K","L","O","P","Z"]
n=int(len(sur))
A=i%n
x=sur[A-1]
print("คนที่โดนตัดออกคือ",x)