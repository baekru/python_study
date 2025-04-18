myStr = "파이썬은 재미있어요. 예외처리 공부"
strPosList = [] #빈리스트
index = 0

while True:
    try:
        index = myStr.index("없는 자료", index)
        strPosList.append(index)
        index = index + 1
    except:
       print("없는 자료 입니다")
       break 
print("파이썬 글자 위치 -->", strPosList)

try:
    num1 = input("숫자1")
    num2 = input("숫자2")

    num1 = int(num1)
    num2 = int(num2)
    res = num1 / num2
    print("결과는", res)
except ZeroDivisionError:
    num2 = input("0으로 나누려고 시도했습니다. num2 다시 입력?")
    res = num1 / int(num2)
    print("결과는", res)
except TypeError:
    print("자료형을 정수형을 입력하세요")
except Exception as e:
    print(type(e).__name__, "에러 났습니다")

# num2를 0으로 입력하면 오류가 난다
# 사용자한테 다시 입력해라100
# 사용자한테 0으로 입력하고 1로 바꿔서 나누게 쓴다.