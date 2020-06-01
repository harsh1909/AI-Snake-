class sb_block :
    def __init__(self,x,y):
        self.sx = x
        self.sy = y
    def display(self):
        print('sx = ',self.sx)
        print('sy = ',self.sy)

block_size = 10
sx = 400
sy = 300
s_size = block_size
head = 0

body = []
body2 = []
            body.insert(0,sb_block(sx,sy))
            body.insert(1,sb_block(sx+block_size,sy))
            body.insert(2,sb_block(sx+2*block_size,sy))
            body.insert(3,sb_block(sx+3*block_size,sy))
            body.insert(4,sb_block(sx+4*block_size,sy))

step = block_size

for i in range(0,5):
    body2.append(sb_block(body[i].sx,body[i].sy))

getche()
        
body[head].sx-=step

for i in range(0,5):
        print('1Block : ',i+1)
        body[i].display()

for j in range(0,5):
        print('2Block : ',j+1)
        body2[j].display()



j=0
for i in range(1,5):
        body[i].sx = body2[j].sx
        body[i].sy = body2[j].sy
        j+=1
for i in range(0,5):
        print('Block : ',i+1)
        body[i].display()
        
        
        
        
        
        df = pd.DataFrame(lis)
    df.to_csv('mamba_data.csv', mode='a', header=False)

import random    
for _ in range(19):
  print(random.randrange(1, 4, 1))
  
  
  
  #convert single observation into test case for prediction single result

a = 618
list = np.array([0,0,a,0,42,2,0,1,1,1,101349.1])
list = list.reshape((1,list.shape[0]))
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)