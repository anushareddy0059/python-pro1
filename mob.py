import re
mob='+91-9876543210'
data=re.findall('\+91-[4789][0-9]{9}',mob)
print(data)