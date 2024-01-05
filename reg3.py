import re
st='AP01AB0987PA32BD8765UP32TH4532'
data=re.findall('AP[0-4]\d[A-Z]{2}\d{4}',st)
print(data)