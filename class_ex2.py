# class person:
#     name = ""
#     age = 0
#     def __init__(self, *args, **kwargs):
#         if args:
#             self.name = args[0]
#             self.age = args [1]
#         if kwargs:
#             self.name = kwargs["name"]
#             self.age = kwargs["age"]
            
# p1 = person("홍길동", 25, "성남시")
# print(p1.name,p1.age)
# p2 = person(name = "이순신", age = 30, address = "서울시") #실인수값이 name="Bob"
# print(p2.name, p2.age)
# p3 = person()
# print(p3.name, p3.age)


class person:
    name = ""
    age = 0
    def __init__(self, *args, **kwargs):
        if args:
            self.name = args[0]
            self.age = args [1]
            self.address = args[2]
        if kwargs:
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.address = kwargs["address"]
            
p1 = person("홍길동", 25, "성남시")
print(p1.name, p1.age, p1.address)
p2 = person(name = "이순신", age = 30, address = "서울시") #실인수값이 name="Bob"
print(p2.name, p2.age, p2.address)
p3 = person()
print(p3.name, p3.age)