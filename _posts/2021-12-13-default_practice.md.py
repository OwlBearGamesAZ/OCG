# def profile(name, age, main_lang):
#     print("이름 : {}\t나이 : {}\t주 사용 언어: {}"\
#         .format(name, age, main_lang))

# profile("선다영", 22, "파이썬")
# profile("도로시", 21, "자바")

# print(profile)
 
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t주 사용 언어: {}"\
        .format(name, age, main_lang))
    

profile("선다영")
profile("도로시")

#중복되는 값을 기본값으로 처리해서 더 간단하게 작성할 수 있다
