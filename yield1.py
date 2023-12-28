b='god father anil'
def sample(b):
    for i in range(0,len(b)):
        if b[i] in 'aeiouAEIOU':
            yield b[i]
            yield i
out=sample(b)
print(out)

            
            
