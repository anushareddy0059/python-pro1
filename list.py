def list(a):
    num=0
    for i in a:
            if type(i)==int:
                  num=num+i
    print(num)
list(['a',1,3,'c',5,13,'e'])
