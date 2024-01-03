import csv
#with open('mca1.csv','w',newline='') as csvfile:
  #  fieldnames=['id','name','mobile','email']
  #  data=csv.DictWriter(csvfile,fieldnames)
  #  data.writeheader()
  # rows=[
    #    {'id':1,'name':'anusha','mobile':987654321,'email':'anu@123'},
    #    {'name':'daffu','id':2,'mobile':123459876,'email':'daffu@321'}

    #]
    #data.writerows(rows)
with open('mca1.csv','r') as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])
        
