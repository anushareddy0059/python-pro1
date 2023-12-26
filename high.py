#to find highest number
a=[1,9,11,23,-65,-78,43]
highest=a[0]
highest1=a[0]
for i in a:
 if highest<i:
   highest=i
for i in a:
   if highest1<i and i!=highest:
    highest1=i
print(highest)
print(highest1)
 