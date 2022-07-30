#리스트
heroes = ["아이언맨","토르", "헐크", "스칼렛 위치"]#[]로 시작과 끝을 나타냄, ','로 각 리스트의 요소를 구분

numbers = []#공백리스트 생성 코드로 항목추가 요소가 많을 경우 요소의 수를 예측하기 쉬워짐
numbers.append(1)#.append로 리스트 마지막 부분에 요소 추가/ '.'은 객체를 의미 객체란 변수와 함수를 묶는 것 (객체.함수 =>객체의 함수를 호출)

list1 = [10,20,"수퍼맨", i ,30, other_list]#숫자 문자열 변수 다른리스트까지 저장하는 혼성리스트 또한 가능

heroes[0]#대괄호 안 숫자는 인덱스를 의미 c언어와 같이 0부터 시작.
heroes[0:3]#0~2까지의 요소를 나타냄(=슬라이싱). 두 번째 인덱스 - 첫 번째 인덱스를 통해 인덱스의 수 계산 가능, 슬라이싱은 리스트의 복사본과 같다
heroes[:3]#0~2까지의 복사본
heroes[3:]#3~마지막까지의 복사본
heroes[:]#모든 요소의 복사본

heroes[1] = "닥터 스트레인지"#인덱스와 등호를 통해 해당 인덱스의 요소 변경 가능
heroes.append("스파이더맨")#리스트의 마지막 부분에 해당 요소를 추가
heroes.insert(1,"배트맨")#해당 인덱스에 해당 요소를 추가.

heroes.remove("스칼렛 위치")#해당 요소를 리스트에서 삭제/ 해당 요소가 리스트에 없을경우 문법오류 발생
if "수퍼맨" in heroes:
    heroes.remove("수퍼맨")#in 연산자를 통해 요소가 리스트안에 있는지 확인 후 삭제
del heroes[0]#del은 인덱스를 사용하여 항목을 삭제
last_heroes = heroes.pop()#리스트의 마지막 요소를 삭제 후 반환

heroes.index("헐크")#해당 요소의 인덱스를 알려준다 / 해당 요소가 리스트에 없을 시 문법 오류 발생
if "헐크" in heroes:
    print(heroes.index("헐크"))#in연산자를 통해 리스트안에 요소가 있는지 확인하는 편이 안전.
for hero in heroes:
    print(hero)#리스트의 모든 요소를 방문할때 사용.
    
heroes.sort()#항목들을 크기순으로 정렬/ 문자열은 알파벳순으로 정렬/ 숫자들은 올림차순으로 정렬
numbers = [9,6,7,1,8,4,5,3,2]
new_list = sorted(numbers)#sort()는 원래의 리스트를 변경한다, 즉 정렬된 새로운 리스트가 반환되는 것이 아니기 때문에 sorted()함수를 사용하여 새로운 리스트를 반환. 즉 정렬전과 정렬후가 공존
new_list = sorted(numbers,reverse=True)#역으로 정렬하고 싶을 때 reverse=True를 추가.

#딕셔너리
phone_book = {}#공백 딕셔너리 '{}'로 생성/ 서로 관련된 키와 값이 함께 저장 => 키-값 쌍(key-value pair)
phone_book["홍길동"] = "010-1234-5678"#공백 딕셔너리에 추가.
phone_book = {"홍길동": "010-1234-5678"}#딕셔너리를 생성하면서 동시에 초기화

print(phone_book["홍길동"])#키를 가지고 연관된 값 찾기의 특화./리스트는 인덱스 딕셔너리는 키가 있어야 값을 찾을 수 있다.
phone_book.keys()#딕셔너리에 있는 모든 키를 출력
phone_book.values()#딕셔너리에 사용되는 모든 값 출력

for key in sorted(phone_book.keys()):#정렬 후 출력
    print(key, phone_book[key])#딕셔너리의 모든 항목을 방문하며 출력
del phone_book["홍길동"]#del을 이용해 딕셔너리의 항목을 삭제
phone_book.clear()#딕셔너리의 모든 항목을 삭제.