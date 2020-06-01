class sb_block :
    def __init__(self,x,y):
        self.sx = x
        self.sy = y
    def display(self):
        print('sx = ',self.sx)
        print('sy = ',self.sy)
        
body = []
body2 = []

      
body.clear()    
body2.clear()    
head = 0

#frame 0

body.insert(0,sb_block(100,200))
body.insert(1,sb_block(110,200))
body.insert(2,sb_block(120,200))
body.insert(3,sb_block(130,200))
body.insert(4,sb_block(140,200))

for i in range(0,5):
    print('Block : ',i+1)
    body2[i].display()
    

#frame 1
body2 = body.copy()
body[head].sx-=10

j=0
for i in range(1,5):
    body[i].sx = body2[j].sx
    body[i].sy = body2[j].sy
    j+=1
    
    
    
body[0].sx
body[head].sy

      
temp = body.copy()
temp[0].display()
body[0].sx-=10

mouse = body[0]
mouse.sx




list = [1,2,3,4,5,]
list
list2 = list.copy()

list[0] +=5 

list.pop()
list2    
    
    
    
    
    
    
    
    
object = sb_block()
object.x

head = sb_block()
body.insert(0,head)
body2 = body.copy()


body.clear()



body = []    
body.append(object)
body.append(1)
body.append(2)
body.insert(3,0)
body.insert(0,4)
body[0]
body.pop()
body[0].x
body[1]











count =1
print('********frame :',count,'************')

283*1.4


list = [{}]
list.append({1,2,3})

l = []
l.append([1,2,3])
l.append([4,5,6])
a = 9
l.append([a,4,4])
print(l)




import csv

lis = []
def writeCsvFile(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items

    Write data to file
    """
    mycsv = csv.writer(open(fname, 'wb'), *args, **kwargs)
    for row in data:
        mycsv.writerow(row)
writeCsvFile(r'd:\tesst.csv', l)

import pandas as pd
df = pd.DataFrame(l)
df.to_csv('filename.csv',mode='a' ,index=False)


