infile = open("C:\\Practice-Python\\chap11\\phones.txt", "r")
#line = infile.readline().rstrip() #readline()은 한번에 한 줄만 읽어 문자열로 반환
#while line != "": #일반적으로 파일에 몇 줄 있는지 모르기 때문에 파일의 크기가 크고 한 줄 씩 읽어서 처리할때 사용.
#    print(line)
#    line = infile.readline().rstrip() #.rstrip()인자로 전달된 문자를 문자열의 오른쪽에서 제거.
#infile.close()

for line in infile: # 이 방법이 더 널리 사용.
    line = line.rstrip()
    print(line)
infile.close()