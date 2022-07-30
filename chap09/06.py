import random

counter = [ 0 , 0 , 0 , 0 , 0 ,0]

for i in range(10000):
    x = random.randint(1,6)
    counter[x-1] += 1
    
for z in range(6):
    print("주사위가 %s인 경우는"%(z+1),counter[z])
    