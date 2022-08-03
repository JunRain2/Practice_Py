infile = open("C:\\Practice-Python\\chap11\\proverbs.txt","r")
for line in infile:
    line = line.rstrip()
    word_list = line.split() #.split() 메소드는 공백문자를 이용하여 문자열에서 단어들을 분리한다.
    for word in word_list:
        print(word);
infile.close()

#import shutil
#shutil.copy("파일1", "파일2")//파일1을 파일2로 복사 하는 함수.