inf = None
inStr = ""
#print (type(inf))
#print (type(inStr))

inF = open("./temp/data.txt", "r", encoding="utf-8")
inStr = inF.readlines()
print(inStr)
inf.close()

with open("./temp/data.txt", "r", encoding="utf-8") as inF:
    inF = inF.readlines()
    print(inStr)
    