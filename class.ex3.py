##########클래스 변수 vs 인스턴스 변수###########
class Dog:
    c_var = "클래스 변수"
    c_i_var = 100
    
    def __init__(self):
        self.c_var = "클래스변수2"  # 여기만 수정 (기존: self.c_ver)
        self.c_i_var = 150
        self.in_var = "인스턴스 변수"
        self.in_i = 200

myDog = Dog()
print(myDog.c_var, myDog.c_i_var, myDog.in_var, myDog.in_i)
print(Dog.c_var, Dog.c_i_var) #클래스안에 맴버 변수
print(myDog.in_var, myDog.in_i)  #생성자안에 변수 출력
#인스턴트 변수는 __init__ 생성자 선언 한 변수이다
#사용하려면 반드시 객체생성해야한다.
#사용하는 방법 myDog.in_ver
#용도 : 필요시에만 사용한다.
#클래스 변수는 class 밑에 써주는 변수명
# 컴파일단계에서 스택 메모리에 올라간다.
# 소멸은 프로그램 종료할때
#용도 : 프로그램 처음부터 끝까지 변수가 유지되어야 할때
#방법 : 클래스명 > Dog.c_var





