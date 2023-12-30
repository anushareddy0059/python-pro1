class Employee:
    company='Tesla'
    ceo='Elon Musk'

    def insert(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid
bhanu=Employee()
vinni=Employee()
DHONI=Employee()
Employee.insert(bhanu,'bhanu',22,50000,201)
Employee.insert(vinni,'vinni',20,40000,200)
DHONI.insert('DHONI',42,100000,202)






