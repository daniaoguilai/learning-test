# massages = ''
# active = True
# while active:
#     massage = input ("what do you want to add :")
#     if massage == 'quit':
#         print (massages)
#         # active = False
#         print(active)
#         break
#     else:
#         massages += massage + ','
#         print(massages)
#         # print(active)
# k = {}
# a = [1, 3, 'q', 'a', 'mn', 'a']
# for z in a:
#     k[z]  = k.get(z,0) + 1
# print(k)
# if 'a' in a:
#     print(1)
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.num = 0
