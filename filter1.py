def data(a):

        if type(a) in(int,float,bool,complex):
            return True
        else:
            return False
res=filter(data,[1,2,2.4])
print(list(res))
