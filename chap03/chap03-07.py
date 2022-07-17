from os import fsencode
import time
fsencode = time.time() #1970년 1월 1일부터 현재까지의 초

days = (fsencode//(60*60*24))%365
hours = (fsencode//(60*60))%24
minit = fsencode//60%60

print(days,"일", hours, "시", minit,"분")