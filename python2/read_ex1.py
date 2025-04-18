#요구사항
#data.txt  파일을 읽어서 화면에 출력하기기
inf = None #자료형이 무엇인지 아직 정해지지 않았다.
#변수를 만들때 무엇엇을 넣을지 미지정(정해지지 않음음)

#문제1
inf = open("./temp/data.txt", "r", encoding="utf-8")
while(True):
    inStr = inf.readline()
    if inStr == "": #true 참이면 EOF (End of file) 이다.
        break
    else:
        print(inStr)
inf.close() #자원반납

#문제2
inf = open("./temp/data_utf8.txt", "r", encoding="utf-8")
while(True):
    inStr = inf.readline()
    if inStr == "": #true 참이면 EOF (End of file) 이다.
        break
    else:
        print(inStr)
inf.close() #자원반납

