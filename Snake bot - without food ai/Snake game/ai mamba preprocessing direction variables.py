#snake body element
class sb_block :
    def __init__(self,x,y):
        self.sx = x
        self.sy = y
    def display(self):
        print('sx = ',self.sx)
        print('sy = ',self.sy)

display_width = 800     #wx
display_height = 600    #wy
block_size = 10
body_size = 16
sx = 400
sy = 300
fx = 100
fy = 300
head = 0
body = []
body.clear()
for i in range(0,body_size):
        body.insert(i,sb_block(sx+i*block_size,sy))


body.append(sb_block(100,300))

#1.WEST
w_wall = body[head].sx

if body[head].sy==fy and body[head].sx>fx:
    w_food = body[head].sx - fx
else:
    w_food = -1
        
for i in range(1,body_size) :
    if body[head].sy==body[i].sy and body[head].sx>body[i].sx:
        w_body = body[head].sx - body[i].sx
    else:
        w_body = -1
        
        
        
#2.NORTHWEST
nw_wall = 1.414*body[head].sx

x = body[head].sx - block_size
y = body[head].sy - block_size
while x > -1 :
    if x==fx and y==fy:
        nw_food = 1.414*(body[head].sx - fx)
        break
    else:
        nw_food = -1
    x = x - block_size
    y = y - block_size

body_found = False
x = body[head].sx - block_size
y = body[head].sy - block_size
while x > -1 :
    for i in range(1,body_size):
        if x==body[i].sx and y==body[i].sy:
            nw_body = 1.414*(body[head].sx - body[i].sx)
            body_found = True
            break
    if body_found==True:
        break
    else:
        nw_body = -1
    x = x - block_size
    y = y - block_size
    
        
        
#3.NORTH
n_wall = body[head].sy

if body[head].sx==fx and body[head].sy>fy:
    n_food = body[head].sy - fy
else:
    n_food = -1
        
for i in range(1,body_size) :
    if body[head].sx==body[i].sx and body[head].sy>body[i].sy:
        n_body = body[head].sy - body[i].sy
    else:
        n_body = -1        
        
        
#4.NORTHEAST
ne_wall = 1.414*body[head].sy

x = body[head].sx + block_size
y = body[head].sy - block_size
while x < display_width+1 and y > -1 :
    if x==fx and y==fy:
        ne_food = 1.414*(body[head].sy - fy)
        break
    else:
        ne_food = -1
    x = x + block_size
    y = y - block_size

body_found = False
x = body[head].sx + block_size
y = body[head].sy - block_size
while x < display_width+1 and y > -1:
    for i in range(1,body_size):
        if x==body[i].sx and y==body[i].sy:
            ne_body = 1.414*(body[head].sy - body[i].sy)
            body_found = True
            break
    if body_found==True:
        break
    else:
        ne_body = -1
    x = x + block_size
    y = y - block_size        

        
#5.EAST
e_wall = display_width - body[head].sx

if body[head].sy==fy and body[head].sx<fx:
    e_food = fx - body[head].sx
else:
    e_food = -1
        
for i in range(1,body_size) :
    if body[head].sy==body[i].sy and body[head].sx<body[i].sx:
        e_body = body[i].sx - body[head].sx
    else:
        e_body = -1        
        
        
#6.SOUTHEAST
se_wall = 1.414*(display_width - body[head].sx)

x = body[head].sx + block_size
y = body[head].sy + block_size
while x < (display_width-1) and y < (display_height-1) :
    if x==fx and y==fy:
        se_food = 1.414*(fx - body[head].sx)
        break
    else:
        se_food = -1
    x = x + block_size
    y = y + block_size

body_found = False
x = body[head].sx + block_size
y = body[head].sy + block_size
while x < display_width-1 and y < display_height-1 :
    for i in range(1,body_size):
        if x==body[i].sx and y==body[i].sy:
            se_body = 1.414*(body[i].sx - body[head].sx)
            body_found = True
            break
    if body_found==True:
        break
    else:
        se_body = -1
    x = x + block_size
    y = y + block_size
        
        
        
#7.SOUTH
s_wall = display_height - body[head].sy

if body[head].sx==fx and body[head].sy<fy:
    s_food = fy - body[head].sy
else:
    s_food = -1
        
for i in range(1,body_size) :
    if body[head].sx==body[i].sx and body[head].sy<body[i].sy:
        s_body = body[i].sy - body[head].sy
    else:
        s_body = -1        
        
        
#8.SOUTHWEST
sw_wall = 1.414*body[head].sx

x = body[head].sx - block_size
y = body[head].sy + block_size
while x > -1 and y < (display_height-1) :
    if x==fx and y==fy:
        sw_food = 1.414*(body[head].sx - fx)
        break
    else:
        sw_food = -1
    x = x - block_size
    y = y + block_size

body_found = False
x = body[head].sx - block_size
y = body[head].sy + block_size
while x > -1 and y < display_height-1 :
    for i in range(1,body_size):
        if x==body[i].sx and y==body[i].sy:
            sw_body = 1.414*(body[head].sx - body[i].sx)
            body_found = True
            break
    if body_found==True:
        break
    else:
        sw_body = -1
    x = x - block_size
    y = y + block_size        
        
        