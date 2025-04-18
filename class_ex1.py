#클래스에서 생성자의 ()괄호 안의 매개변수(가매개변수)의 갯수를 유동적으로 하려면 *매개변수 명이 들어가야한다
# *매개변수 - 튜플형식으로 저장됨
# **매개변수 - 딕셔너리형식으로 저장됨
class Car:
    #맴버필드드
    color = ""
    price = 0
    speed = 0
    #생성자 : 객체생성 Car() 할때 자동으로 호출된 곳
    def __init__(self, *v1):
        for i in range(len(v1)):
            if(i==0):
                self.color = v1[0]
            if(i==1):
                self.price = v1[1]
            if(i==2):
                self.speed = v1[2]
                
myCar1 = Car ("빨강", 1000, 30)
print(myCar1.color, myCar1.price, myCar1.speed)       
myCar2 = Car ("파랑", 2000)
print(myCar2.color, myCar2.price, myCar2.speed)   
myCar3 = Car ("노랑")   
print(myCar3.color, myCar3.price, myCar3.speed)

class Car:
    color = ""
    price = 0
    speed = 0

    def __init__(self, v1=("흰색", 100), v2=10):
        # v1: (색상, 가격), v2: 속도
        self.color = v1[0]
        self.price = v1[1]
        self.speed = v2

############## # ---- 사용 예시 ----GPT 코드####################
# # 인자 없이 호출 → 기본값 ("흰색", 100), 속도 10
# myCar1 = Car()
# print(myCar1.color, myCar1.price, myCar1.speed)  
# # 출력: 흰색 100 10

# # (빨강, 200) 튜플을 넘기고, 속도를 50으로
# myCar2 = Car(("빨강", 200), 50)
# print(myCar2.color, myCar2.price, myCar2.speed)
# # 출력: 빨강 200 50

# # (파랑, 300)만 주면 속도는 기본값 10
# myCar3 = Car(("파랑", 300))
# print(myCar3.color, myCar3.price, myCar3.speed)
# # 출력: 파랑 300 10
