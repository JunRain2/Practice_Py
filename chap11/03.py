#outfile = open("C:\\Practice-Python\\chap11\\phones1.txt","w") #w 모드는 기존의 데이터는 사라지고 새로운 데이터로 대체.

outfile = open("C:\\Practice-Python\\chap11\\phones1.txt","a") #a 모드는 기존의 데이터에 새로운 데이터를 이어붙임.

outfile.write("Hong 010-1234-5678\n")
outfile.write("Kim 010-1234-5679\n")
outfile.write("Lee 010-1234-5680\n")

outfile.close()
