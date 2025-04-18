############1단계 설계한다.
class Car:
    #필드 : 클래스 안에 선언한 변수
    #맴버 필드
    color = ""
    speed = 0
    # mathod 매소드: 클래스 안에 선언한 함수
    def upSpeed(self, value):  #self 자기 자신
        self.speed = self.speed + value
    def downSpeed(self, value) :
        self.speed = self.speed - value
    def __init__(self, v1="흰색", v2=5): #생성자
        #생성자의 용도 : 객체생성하면 기본값을 셋팅함
        self.color = v1
        self.speed = v2

# ############2단계 인스턴트(객체)화 한다.
myCar = Car()    #java 문법 Car myCar = new Car()
print(myCar.color)
print(myCar.speed)

myCar2 = Car("빨강", 30)
print(myCar2.color)
print(myCar2.speed)

myCar3 = Car("파란", 50)
print(myCar3.color)
print(myCar3.speed)

myCar4 = Car("노랑", 70)
print(myCar4.color)
print(myCar4.speed)

# #번수가 "노랑" 하나만 있을시 출력 오류발생.*2개를 요청했으면 2개에 대한 변수를 넣어줘야함함
# myCar4 = Car("노랑")
# print(myCar4.color)
# print(myCar4.speed)

# myCar2 = Car()
# myCar3 = Car()

# #3번째 단계 *변수값,함수 호출,출력하여 사용한다.
# myCar.color = "빨강"
# myCar.speed = 350

# myCar2.color = "흰색"
# myCar2.color = 280

# myCar3.color = "검정색"
# myCar3.color = 300

# myCar.downSpeed(150)
# print(myCar.speed)


########## 클래스의 완전한 작동 구현

# 1단계  클래스 선언 
# 2단계  인스턴스 생성
# 3단계  필드나 메서드 사용

# ## 클래스 선언 부분 ##
# class  Car :
#     color = ""
#     speed = 0

#     def  upSpeed(self, value) :
#         self.speed += value
    
#     def  downSpeed(self, value) :
#         self.speed -= value

# ## 메인 코드 부분 ##
# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar3 = Car()
# myCar3.color = "노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))

# myCar2.upSpeed(60)
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

# myCar3.upSpeed(0)
# print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))


