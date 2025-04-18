import os
inFp = None
fName = ""
intist = []
inStr = ""
while(True):
    fName = input("파일명을 입력하세요?")
    if(os.path.exists(fName)):
        with open(fName, "r") as inFp:
            inList = inFp.readlines()
        print(inList)
        break
    else:
        print("파일이 없습니다")
    
#만약에 파일이 없다면 다시 파일이 입력되게 코드 만들기
