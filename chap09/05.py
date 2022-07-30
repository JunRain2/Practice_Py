number = []

for i in range(5):
    x=int(input("정수를 입력하시오 :"))
    number.append(x)

z=0
for y in number:
    z +=y
    
print("평균 %s"%(z/5))