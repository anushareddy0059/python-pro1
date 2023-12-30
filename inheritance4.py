class add3:
   @staticmethod
   def add3(a,b,c):
      return a+b+c
class add2:
   @staticmethod
   def add2(a,b):
      return a+b
class add(add3,add2):
   pass
class sub:
   @staticmethod
   def sub(a,b):
      return a-b
class cal(add,sub):
   pass
obj=cal()