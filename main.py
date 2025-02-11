# ism = input("ismingiz: ")
# fam = input("familyangiz: ")

# def ism_chiqar():
#     print(f"ism: {ism}")
#     print(f"familya: {fam}")

# ism_chiqar()


# def fun():
#     for i in range(1,11):
#         if i != 5:
#             print(i)

# fun()



# def fun():
#     for i in range(1,101):
#         if i % 3 ==0 and i >= 15 and i <= 20:
#             print(i)

# fun()  
   

# n = input("n soni kirit")

# def aniqlash(malumot):
#     if isinstance(malumot, int):
#         return "Bu butun son."
#     elif isinstance(malumot, float):
#         return "Bu o'nlik son."
#     elif isinstance(malumot, str):
#         return "Bu matn."
#     elif isinstance(malumot, list):
#         return "Bu ro'yxat."
#     elif isinstance(malumot, dict):
#         return "Bu lug'at."
#     elif isinstance(malumot, tuple):
#         return "Bu tupla."
#     elif isinstance(malumot, bool):
#         return "Bu mantiqiy qiymat."
#     else:
#         return "Bu boshqa turdagi ma'lumot."


# print(aniqlash(n))  




# def kub (num1):
#     return num1 **2
# print(kub(3))

# def kub (num1):
#     return num1 **3
# print(kub(3))

# def kub (num1,num2):
#     return num1 **num2
# print(kub(3,9))


# name = input("ism kirit:")
# surname = input("familya kirit:")
# age =int(input("yoshizni kiriting:"))

# def katta(name):
#     print(name.capitalize())

# print(katta(name))


# 1-misol
# text =["Uzun","olma","Anor","Shaftoli","olcha"]

# def katta_harf(text):
#     counter = 0
#     for i in text:
#         if i >= "A" and i <= "Z":
#             counter += 1 
#     return counter

# print(katta_harf(text))



#1-misol
# son = input("soni kiriting: ")

# lst = [10,"13",35,3,433]# 3 soni 5ta



# for i in lst:
#     if str(i) == son:
#         print(True)
#         break
#     else:
#         print(False)



#2-misol


# for i in range(100,999):

#     b = i % 10
#     o = i / 10 % 10
#     y = i / 100 % 10

#     j = b+o+y

#     if j > 5 and j < 8:
#         print(i)


#3-misol

# son = input("son kiriting: ")# 34

# print(len(son))

#4-misol

# son = int(input("son kirit "))

# b = son % 10
# o = son / 10 % 10
# y = son / 100 % 10
# m = son / 1000 % 10

# print(int(b+o+y+m))


#5-misol


# katta = 0

# for i in range(1,4):
    
#     son = int(input(f"{i}-son kiriting:")) # 10
#     if son > katta:
#         katta = son

# print(katta)


#6-misol
# son = int(input("1-sonni kiriting:")) # 4

# kichik = son

# for i in range(2,5):  
#     son2 = int(input(f"{i}-son kiriting:")) # 4 

#     if son2 < kichik:
#         kichik = son2

# print(kichik)


#7-masala 

# lst =[1,2,3,4,5,6]

# for i in lst:
#     s =lst[i-1]
#     print(s*2)

#8-masala
 
# for i in range(-10,10):

#     if i % 3 == 1:
#         print(i)






#1-masala

# for i in range(20):
#     if i == 4 or i == 9 or i == 14 or i ==19:
#         print("\n")
#         continue
#     print("*", end=" ")
    
    
#2-masala
# for i in range(16): 
#     if i == 0 or i == 4 or i == 8 or i == 12 or i == 16:
#         if i  == 4 or i == 8 or i == 12 or i == 16:            
#             print("\n")
#             print("#", end=" ")
#             continue
#         print("#", end=" ")
#         continue

#     print("*", end=" ")

#3-masala
# for i in range(20):
#     if i >= 0 and i <= 3 :
#         print("#",end=" ")
#         if i == 3:
#             print("\n")
#         continue
#     if i == 4 or i == 8 or i == 12 or i == 16:
#         if i  == 4 or i == 8 or i == 12 or i == 16:            
#             print("\n")
#             print("#", end=" ")
#             continue
#         print("#", end=" ")
#         continue

#     print("*", end=" ")

#4-masala
# for i in range(17):
#     if i >= 0 and i <= 3:
#         print("#",end=" ") 
#         continue 
#     if i == 4:
#         print("\n")
#         continue
    
#     if i == 5 or i == 9 or i == 13 or i == 17:
#         if i  == 5 or i or== 9  i == 13 or i == 17:            
#             print("\n")
#             print("#", end=" ")
#             continue
#         print("#", end=" ")
#         continue
#     if i  == 8 or i == 12 or i == 16 :            
#             # print("\n")
#             print("#", end=" ")
#             continue

#     print("*", end=" ")
    
#5masala

# for i in range (16): #qator
#     for j in range(16):#ustun
#         if i == j:
#             if i == 5 or i == 6 or i == 9 or i == 10 :
#                 print("*", end=" ")
#             else:
#                 print("#",end=" ")
#             if i == 3 or i == 7 or i == 11 or i == 15:
#                 print("\n")


#6masala
# for i in range (20): #qator
#     for j in range(20):#ustun
#         if i == j:
#             if i == 5 or i == 6 or i == 13 or i == 14 :
#                 print("*", end=" ")
#             else:
#                 print("#",end=" ")
#             if i == 3 or i == 7 or i == 11 or i == 15:
#                 print("\n")

#7masala
# for i in range (20): #qator
#     for j in range(20):#ustun
#         if i == j:
#             if i == 5 or i == 6 or i == 13 or i == 14 :
#                 print("0", end=" ")
#             else:
#                 print("#",end=" ")
#             if i == 3 or i == 7 or i == 11 or i == 15:
#                 print("\n")

#8masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
#             if i == 0 or i == 6 or i == 12 or i == 18 or i == 24 :
#                 print("0", end=" ")
#             else:
#                 print("#",end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                 print("\n")

#9masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
#             if i == 0 or i == 5 or i == 6 or i == 10 or i == 11 or i == 12 or i == 15 or i == 16 or i == 17 or i ==18 or i >19 :
#                 print("0", end=" ")
#             else:
#                 print("#",end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                 print("\n")

#10-masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
#             if i % 2 == 0:
#                 print("0", end=" ")
            
#             else:
#                 print("1", end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                     print("\n")


#11-masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
#             if i % 2 == 0 :
#                 if i == 0 or i == 4 or i == 6 or i == 8 or i == 12 or i == 16 or i==18 or i ==20 or i ==24:
#                     print("0", end=" ")
#                 else:
#                     print("1", end=" ")
            
#             else:
#                 print("1", end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                     print("\n")

#12-masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
#             if i % 2 == 0:
#                 print("0", end=" ")
            
#             else:
#                 print("1", end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                     print("\n")


#11-masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:
            

#             if i == 7 or i == 11 or i == 13 or i == 17:
#                  print("1", end=" ")            
#             else:
#                 print("0", end=" ")
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                 print("\n")
            


#12-masala

# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:            

#             if i >= 0 and i <= 4:
#                  print("A", end=" ") 
#             elif i >= 5 and i <= 9:
#                  print("B", end=" ")  
#             elif i >= 10 and i <= 14:
#                  print("C", end=" ") 
#             elif i >= 15 and i <= 19:
#                  print("D", end=" ") 
#             elif i >= 20 and i <= 24:
#                  print("E", end=" ")           
            
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                 print("\n")

#13-masala
# for i in range (25): #qator
#     for j in range(25):#ustun
#         if i == j:            

#             if i == 0 :
#                  print("1", end=" ") 
#             elif i == 2 :
#                  print("2", end=" ")  
#             elif i == 3 :
#                  print("3", end=" ")  
#             elif i == 4 :
#                  print("4", end=" ")  
#             elif i == 5 :
#                  print("5", end=" ")  
#             elif i == 6 :
#                  print("6", end=" ")  
#             elif i == 7 :
#                  print("7", end=" ")  
#             elif i == 8 :
#                  print("8", end=" ")                 
            
#             if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
#                 print("\n")



# lst = [22,21,31,23,33,42,44]

# l =[]
# for i in lst:
#     if i % 11 == 0:
#       print(i)



# def fun1(num1,num2):
#     return(num1+num2)


# a = fun1

# print(a(10,20))


# def fun2(ism,fam):
#     return(ism, " ", fam)


# b = fun1

# print(b("Atamjon","Raximov"))


# def fun1(num1,num2):
#     return(num1%num2 ==0)


# a = fun1

# print(a(10,20))




#1-masala
# import random


# def son ():
#     r = random.randint(1,10)
#     return r

# print(son())


#2-masala
# lst=[3,232,434,3,44,552,323,0]

# def katta(lst):
#     k = max(lst)
#     return k


# print(katta(lst))


#3-masala

# def r ():
#     for i in range(1,34621):    
#         return i

# random = r

    

# def kichik (son):
#     k =min(son)
#     return k

# print(kichik(random))


#4-masala

# matn =input("hard kirit katta harfni topib beraman: ")

# def katta(matn):
#     sanoq = 0
#     for i in matn:
#         if i >= "A" and i <= "Z":
#             sanoq+=1
    
#     return sanoq

# print(katta(matn))


#5-masala
# matn =["1ab2c3"]

# def dicyasa(matn):
#     dict={
#         }
    
#     for i in matn:
#         dict[i]="wdfw"
        

# print(dicyasa(matn))

# def yuza(a,b):
#     return a*b

# def hajm(h,yuza):
#     return h*yuza


# print(hajm(5,yuza(3,4)))

#colbacks 2masala
# def juft(number):
#     if number % 2 == 0:
#         return("True")
#     else:
#         return("False")


# def check_conditions(number,juft):
#     return(juft(number))

# num = int(input("soni kiriting:"))
# print(check_conditions(num,juft))


# argusni o'rganib kelish


#1-misol
# def yigindi(a,*argus):
#     print(sum(argus)+a)

# yigindi(5,10,5,20)


#2-misol
# def user_info(name,**kvargs):
#     for key, value in kvargs.items():
#        name += f"{key},{value}"
#     return name
      
    

# print(user_info("Atamjon",yosh=32,kasbi="doktor"))


#3-misol
# def kopaytma(*argus):
#     a = 1
#     for i in argus:
#         a*=i
    
#     print(a)

# kopaytma(2,2,2)

#4-misol
# def datalar(*argus,**kvargus):
#     a = sum(argus)
#     b =sum(kvargus)
   
#     m =max(argus)
#     print(m)
#     print(a+b)
        
# datalar(10,20,30)


#5-misol
# def filtrKey(**kvargs):
#     dict={}
#     for key,value in kvargs.items():
#         if len(key) > 3:
#             dict[key] =value
            
#     print(dict)

# filtrKey(name="atamjon",age=18,job="teacher")

# a=[1,2]
# b=[2,1]

# b[0],a[0]=a[0],b[0]
# print(a,b)




# def fib(n):
#     if n == 1:
#         return n
#     if n == 0:
#         return n
#     return fib(n-1)+fib(n-2)


# print(fib(50))


# x =12


# def f1(a,b=x):
#     print(a,b)
    

# x= 15

# f1(4)


# x =10
# a=lambda y: x+y
# x=20
# b=lambda y : x+y

# print('{},{}'.format(a(10),b(10)))



# s= lambda x:lambda x:lambda x:x+7

# r = s(30)(20)(0)

# print(r)


# a=["a","b","c"]
# b=a.copy

# a.append("d")
# print(a==b)


#1misol

# lst = [1,2, [3, 4, [5], 6], [7, [8, [9]]]]



# def rekursiya(n_list):
#     result = []
#     for i in n_list:
#         if isinstance(i, list): 
#             result.extend(rekursiya(i)) 
#         else:
#             result.append(i) 
#     return result


# print(rekursiya(lst))  



#2-misol
# dct = {
#     1: [1, 2, ["Hello"], "Привет"],
#     2: (1, 2, 3, (1,)),
#     3: "Salom",
#     4: {1, 2, 3},
#     5: 12345
# }


# def new_dict(n):
#     result = []
#     if isinstance(n, dict):
#         for key, value in n.items():
#             result.extend(new_dict(value))
#     elif isinstance(n, (list, tuple, set)):
#         for i in n:
#             result.extend(new_dict(i))
#     else:
#         result.append(n)
#     return result





# print(new_dict(dct))  



#3-misol
# lstText = [
#     'Tommy',
#     ["Anna", "John"], "George",
#     "Alisher", "Umar", "Muhammad", ['Umarali', "Abubakr"]
# ]

# def unli(lst):
#     result=[]
#     for i in lst:
        
#         if i == "a" or i =="o" or 
#          if isinstance(lst, list):
#              result.extend(i)
#     return result

# print(unli(lstText))
        
        
        
# with open("example.txt", "w") as file:
#     file.write("Bu imtihonga tayyorlanish uchun matn.")