inF, outF = None, None
inStr = ""  # 바이너리 데이터니까 문자열 말고 바이트로 초기화
source = input("소스파일명을 입력하세요")
taget = input("타깃 파일명을 입력하세요")

inF = open(source, "rb")         # 텍스트가 아닌 바이너리 모드로 읽기
outF = open(taget, "wb")   # 바이너리 모드로 쓰기
'''''
while True:
    inStr = inF.read(1024)  # 바이트 단위로 읽기 (한 번에 1KB)
    if inStr == b"":        # 빈 바이트면 EOF
        break
    else:
        outF.write(inStr)   # 그대로 복사
'''''
for i in inF.readlines():
    outF.write(i)
inF.close()
outF.close()
   