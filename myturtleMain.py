from myTurtle import *
import turtle

# 기본 설정
inStr = ''
swidth, sheight = 600, 600
tX, tY, tAngle, txtSize = [0] * 4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)

# 0.0 ~ 1.0 범위의 float RGB 모드를 사용 (중요)
turtle.colormode(1.0)

# 배경색은 선택 사항(색상 변화를 잘 확인하고 싶다면 어두운 배경이 유리)
# turtle.bgcolor('black')

turtle.penup()
turtle.speed(5)

# 문자열 한 번만 입력받기
inStr = getString()

# 문자열 내 각 글자를 무작위 위치/각도/크기/색으로 출력
for ch in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)  # 좌표, 각도, 글자 크기
    r, g, b = getRGB()                                  # 색상 (0.0~1.0 범위)

    turtle.goto(tX, tY)
    turtle.left(tAngle)
    turtle.pencolor(r, g, b)                            # 펜 색상 설정
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()
