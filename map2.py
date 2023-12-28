
def main(a):
    if type(a) in [int,float,bool,complex]:
        return a
    else:
        return len(a)
       
res=map(main,[1,(4,5),[7,9],{1:2}])
print(list(res))