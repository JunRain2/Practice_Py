import pickle

file = open("C:\\Practice-Python\\chap11\\save.p", "rb") #rb : 이진파일 읽기
obj = pickle.load(file) #load를 통해 파일에 저장된 딕셔너리를 복원
print(obj)
file.close()

#pickle 객체는 파이썬 객체를 직렬화하고 역 직렬화하는 프로트콜을 구현. dump()호출시 파이썬 객체 -> 바이트 스트림, load()호출시 바이트 스트림 -> 파이썬 객체.