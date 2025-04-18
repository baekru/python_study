try:
    inF = None
    inF=open("./temp/data2.ddd", "r", encoding="utf-8")
except FileNotFoundError:
    print( "파일은 없습니다") 
else :
    inList = inF.readlines()
    print(inList)   
finally :   
    if( inF != None) :    
        inF.close() 