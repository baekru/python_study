def outFunc(v1, v2) :
    def inFunc(num1, num2) :
        return num1 + num2
    return inFunc(v1, v2)

print(outFunc(10,20))

def selfCall() :
    print('ha', end='')
    selfCall()

def count(num) :
   if (num >= 1):
       print(num, end = '')
       count(num-1)
   else :
      return

count(10)

def genFunc() :
    yield 1
    yield 2
    yield 3

print(list(genFunc()))

def genFunc(num) :
    for i in range(0,num) :
        yield i
        print('제너레이터 진행 중..')

for data in genFunc(5) :
    print(data)