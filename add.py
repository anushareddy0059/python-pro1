a='abc123@789'
out=0
for var in a:
    if '0'<=var<='9':
        out=out+int(var)
print(out)