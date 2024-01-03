st=input('')
temp=st.split('.')
if len(temp)==4:
    for i in temp:
        if i.isnumeric():
            out+='yes'
        else:
            out='no'
            break
    else:
        out='no'
print(out)