import random
time = random.randint(1,24)
sunney = random.choice([True, False])
print("좋은 아침입니다. 지금 시각은 %s시 입니다" % time)
if sunney:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

if sunney == True and (time>=6 and time<9):
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")
    
