print (ord('파')) #ord("문자") 문자의 유니코드값 변환
num = ord('파')
print(chr(num)) #chr(숫자)
#숫자에 해당되는 유니코드 문자 반환
aa = chr(num + 100) #54128
num = ord(aa)
print(chr(num-100))

inF, outF = None, None
inStr, outStr = "", ""
i = 0
secu = 0

secuYn = input("1.암호화 2.암호해석 선택?")
inFname = input("입력 파일명을 입력하세요")
outFname = input("출력 파일명을 입력하세요")

if (secuYn == '1'):
    secu = 100
elif (secuYn == '2'):
    secu = -100
inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding="utf-8")
while True:
    inStr = inFp.readline()
    if not inStr:
        break
    outStr = ""
    for i in range(0,len(inStr)):
        ch=inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2
    outFp.write(outStr)
outFp.close()
inFp.close()
print('%s --> %s 변환 완료' % (inFname, outFname))