import pickle #딕셔너리와 같은 개체를 파일에 저장하기 위해서 사용.

gameOption = {"sound": 8, "VideoQuality": "HIGHT", "Money" : 100000, "WeaponList":["gun","missile","knife"]}

file = open("C:\\Practice-Python\\chap11\\save.p","wb") #이 파일안에 새로운 내용을 써야 하기 때문에 어떤 파일이름이나 확장자로도 사용 가능.//wb는 이진 파일 쓰기모드
pickle.dump(gameOption, file) #dump() : 객체를 pickle 모듈로 압축/ dump()함수는 파일 객체를 필요로 한다./ 
file.close()