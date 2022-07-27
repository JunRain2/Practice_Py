plain_text = "Love will find a way."
encrypted_text=""
for c in plain_text:#plain_text안의 리스트가 끝날 때 까지
    x = ord(c)#문자의 코드값
    x = x+1#코드값 + 1
    cc = chr(x)#코드값을 문자로 반환
    encrypted_text = encrypted_text + cc#계속 추가해 나가야 하기 때문 
print(encrypted_text)

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x-1
    cc = chr(x)
    plain_text = plain_text + cc
    
print(plain_text)