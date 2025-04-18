def main():
    print("계산기 프로그램입니다. 두 개의 숫자를 입력하세요.")

    # 첫 번째 숫자 입력
    num1 = float(input("첫 번째 숫자를 입력하세요: "))

    # 연산자 입력
    op = input("연산자(+, -, *, /)를 입력하세요: ")

    # 두 번째 숫자 입력
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 입력된 연산자에 따라 연산 수행
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        # 0으로 나눌 경우 에러 처리
        if num2 == 0:
            print("오류: 0으로 나눌 수 없습니다.")
            return
        result = num1 / num2
    else:
        print("지원하지 않는 연산자입니다. (+, -, *, /) 중 하나를 사용하세요.")
        return

    # 결과 출력
    print("계산 결과:", result)

if __name__ == "__main__":
    main()
