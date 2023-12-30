class Grand:
  def __init__(self,b):
    self.b=b
class parent(Grand):
  def __init__(self,b,c,d):
    super().__init__(b)
    self.c=c
    self.d=d
class derived(parent):
  def __init__(self,b,c,d,e):
    super().__init__(b,c,d)
    self.e=e
obj=derived(12,13,14,15)

