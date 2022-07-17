num = int(input("정수를 입력 하시오 : "))
n = 4

first = num//1000
second = (num%1000)//100
third = (num%100)//10
last = num%10

sum = first + second + third + last

print("자리수의 합 : ",sum)