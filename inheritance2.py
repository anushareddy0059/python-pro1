class Collage:
  def __init__(self,mca):
    self.mca=mca
class mba(Collage):
      def __init__(self,mca,sec1,sec2):
        super().__init__(mca)
        self.sec1=sec1
        self.sec2=sec2
class degree(Collage):
      def __init__(self,mca,sec1,sec2,bsc):
        super().__init__(mca,sec1,sec2)
        self.bsc=bsc
obj=degree(60,12,14,15) 


