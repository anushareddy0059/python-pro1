import re
pan='ABCDE1234FERTFS4532DAERDC4567DASHN4567RSDEFG6789G'
data=re.findall('[A-Z]{5}\d{4}[A-Z]',pan)
print(data)

