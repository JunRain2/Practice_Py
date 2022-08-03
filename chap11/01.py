infile = open("C:\\Practice-Python\\chap11\\phones.txt", "r")#infile은 파일 객체/ open()은 파일 이름을 받아서 파일 객체를 생성한 후에 반환한다.//파일을 여는데 실패시 None 객체가 반환
#"r"읽기모드, "w"쓰기모드, "a"추가모드, "r+"읽기와 쓰기 모드(모드를 변경하려면 seek()를 호출)

#lines = infile.read() #.read()는 파일의 데이터를 읽는 매소드. 지정된 개수의 문자를 읽고 싶을 때는 괄호안에 정수를 입력.
lines = infile.readlines() #.readlines(): 파일에서 전체 데이터를 읽는 함수. 각각의 줄이 리스트에 저장. 하나의 항목이 하나의 요소.
infile.close() #파일을 열었으면 닫아야한다. 파일을 열어서 사용 할 경우 다른 프로그램이 파일로 접근이 불가.
print(lines)