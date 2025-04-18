import shutil
print(dir(shutil))

#shutil.copy("./temp/in.txt", "./temp/copy_in.txt")
#shutil.move("./temp/in.txt", "./in.txt")

import os

if(not os.path.exists("./temp/sss")):
    os.mkdir("./temp/sss")

if os.path.exists("./temp/mm"):
    shutil.rmtree("./temp/mm")
#해당 폴더 안에 파일목록들 보기

for dirName, subDirList, Fnames in os.walk("./temp"):
    for fname in Fnames : 
        print(os.path.join(dirName, fname))
    for s in subDirList:  #하위 폴더 출력
        print(s)

if (os.path.exists("./temp/data1.txt")):
    os.remove("./temp/data1.txt")
#a.mp4 파일 크기 알기

if (os.path.exists("./temp/a.mp4")):
    file_size = os.path.getsize("./temp/a.mp4")
    print("%.2f %s" % (file_size / 1024 / 1024, 'mb'))    
    
#파일을 압축하기
import zipfile
newZip = zipfile.ZipFile("./new.zip", "w")
newZip.write("./temp/a.mp4", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

#압축된 파일을 풀기
extZip = zipfile.ZipFile("./new.zip", "r")
extZip.extractall("./temp/ss")
extZip.close()