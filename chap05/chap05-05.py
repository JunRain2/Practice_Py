id = "ilovepython"
pw = "123456"

input_id = input("아이디를 입력하시오 : ")
if input_id == id :
    input_pw = input("비밀번호를 입력하시오 : ")
    if input_pw == pw :
        print("환영합니다.")
    else :
        print("패스워드를 잘못 입력하였습니다.")
else:
    print("아이디를 잘못 입력하였습니다.")