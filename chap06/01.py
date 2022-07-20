import random
number = random.randint(1,100)
in_number = 0
count = 0

while in_number != number:
    in_number = int(input("숫자를 입력하시오 : "))
    if in_number < number:
        print("낮음!")
    if in_number > number:
        print("높음!")
    count += 1
        
print("축하합니다. 시도횟수= %s" % count)