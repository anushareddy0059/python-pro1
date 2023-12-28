def upper(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
res=filter(upper,'aBc@15$67DEfgh')
print(list(res))
