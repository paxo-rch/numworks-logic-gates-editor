from math import *
from kandinsky import *
from ion import *
from time import *

tyAnd=0
tyOr=1
tyNot=2
tyIn=3
tyOut=4

class C:
  def __init__(self):
    self.x=160
    self.y=111

c=C()

p=[]

sl=None

slF=None
slFi=0

slT=None
slTi=0


class L:
  def __init__(self,t):
    p.append(self)
    self.t=t
    self.x=0
    self.y=0
    
    self.in1=[None,False]
    self.in2=[None,False]
    self.ou1=[None,False]
    
    self.e=True
  
  def draw(self):
    if(self.t==tyAnd or self.t==tyOr):
      fill_rect(c.x+self.x,c.y+self.y+10,5,5,[int(slF==self and slFi==0)*248,int(self.in1[1])*252,0])
      fill_rect(c.x+self.x,c.y+self.y-10,5,5,[int(slF==self and slFi==1)*248,int(self.in2[1])*252,0])
      fill_rect(c.x+self.x+40,c.y+self.y,5,5,[int(slT==self)*248,int(self.ou1[1])*252,0])

    if(self.t==tyAnd):
      draw_string("and",c.x+self.x+5,c.y+self.y-7,[int(sl==self)*248,0,0])
    if(self.t==tyOr):
      draw_string("or",c.x+self.x+5,c.y+self.y-7,[int(sl==self)*248,0,0])
    if(self.t==tyNot):
      draw_string("not",c.x+self.x+5,c.y+self.y-7,[int(sl==self)*248,0,0])

    if(self.t==tyNot):
      fill_rect(c.x+self.x,c.y+self.y,5,5,[int(slF==self)*248,int(self.in1[1])*252,0])
      fill_rect(c.x+self.x+40,c.y+self.y,5,5,[int(slT==self)*248,int(self.ou1[1])*252,0])
      
    if(self.t==tyIn):
      fill_rect(c.x+self.x-10,c.y+self.y-10,20,20,[int(self.ou1[1])*248,0,0])
    
    if(self.in1[0]!=None):
      if(self.t==tyNot):
        draw_line(c.x+self.in1[0].x+(40+2)*int(self.in1[0]!=None and self.in1[0].t!=tyIn),c.y+self.in1[0].y+2,c.x+self.x,c.y+self.y+2,[0,0,0])
      else:
        draw_line(c.x+self.in1[0].x+(40+2)*int(self.in1[0]!=None and self.in1[0].t!=tyIn),c.y+self.in1[0].y+2,c.x+self.x,c.y+self.y+10,[0,0,0])
    if(self.in2[0]!=None):
      draw_line(c.x+self.in2[0].x+(40+2)*int(self.in2[0]!=None and self.in2[0].t!=tyIn),c.y+self.in2[0].y+2,c.x+self.x,c.y+self.y-10,[0,0,0])
  
  def update(self):
    if(self.in1[0]!=None and self.in1[0].e==False):
      self.in1[0]=None
    if(self.in2[0]!=None and self.in2[0].e==False):
      self.in2[0]=None
    
    if(self.in1[0]!=None):
      self.in1[1]=self.in1[0].ou1[1]
    if(self.in2[0]!=None):
      self.in2[1]=self.in2[0].ou1[1]
    
    if(self.t==tyAnd):
      self.ou1[1] = (self.in1[1] and self.in2[1])
    if(self.t==tyOr):
      self.ou1[1] = (self.in1[1] or self.in2[1])
    if(self.t==tyNot):
      self.ou1[1] = not self.in1[1]
    
    if(self.t==tyIn):
      self.ou1[1] = self.in1[1]
    
def load():
  with open("save.py","r") as f:
    nn=[]
    for i in f.read().split("\n"):
      s=i.split(",")
      n=[]
      try:
        for i in s:
          n.append(int(i))
        nn.append(n)
        nl=L(n[2])
        nl.x=n[0]
        nl.y=n[1]
      except:
        pass
    for i,v in enumerate(p):
      if(nn[i][3]!=-1):
        p[i].in1[0]=p[nn[i][3]]
      if(nn[i][4]!=-1):
        p[i].in2[0]=p[nn[i][4]]
      if(nn[i][5]!=-1):
        p[i].ou1[0]=p[nn[i][5]]

load()
def save():
  with open("save.py","w") as f:
    f.write("0")
    for i in p:
      i1=-1
      i2=-1
      o=-1
      if(i.in1[0]!=None):
        i1=p.index(i.in1[0])
      if(i.in2[0]!=None):
        i2=p.index(i.in2[0])
      if(i.ou1[0]!=None):
        print(p,i.ou1[0])
        o=p.index(i.ou1[0])
      f.write(str(i.x)+","+str(i.y)+","+str(i.t)
      +","+str(i1)
      +","+str(i2)
      +","+str(o)
      +"\n")

if(len(p)==0):
  l=L(tyAnd)

def getl():
  md=1000
  mi=0
  
  for i,o in enumerate(p):
    if(md>sqrt((160-c.x-o.x)**2+(111-c.y-o.y)**2)):
      md=sqrt((160-c.x-o.x)**2+(111-c.y-o.y)**2)
      mi=i
  return [p[mi],mi]

sl=getl()[0]
  
while True:
  m=False
  move=int(keydown(KEY_OK) and sl!=None)
  
  if(keydown(KEY_ALPHA)):
    save()
  if(keydown(KEY_PLUS)):
    m=True
    if(sl==slF):
      slFi=(slFi+1)%2
    sleep(0.3)
  
  if(keydown(KEY_MINUS)):
    m=True
    if(slF!=None and slT!=None):
      if(slF.t!=tyNot and slF.t!=tyIn):
        if(slFi==0):
          slF.in1[0]=slT
        else:
          slF.in2[0]=slT
      else:
          slF.in1[0]=slT
  
  if(keydown(KEY_DOT)):
    m=True
    if(sl.t==tyIn):
      sl.in1[1]=not sl.in1[1]
      sleep(00.2)
    elif(slF!=None):
      if(slF.t!=tyNot):
        if(slFi==0):
          slF.in1[1] = not slF.in1[1]
        else:
          slF.in2[1] = not slF.in2[1]
      else:
          slF.in1[1] = not slF.in1[1]
      
      sleep(0.5)      
  
  if(keydown(KEY_TOOLBOX)):
    m=True
    draw_string("1=and 2=or 3=not",0,0)
    n=0
    while True:
      if(keydown(KEY_ONE)):
        n=1
        break
      if(keydown(KEY_TWO)):
        n=2
        break
      if(keydown(KEY_THREE)):
        n=3
        break
      if(keydown(KEY_FOUR)):
        n=4
        break
      if(keydown(KEY_FIVE)):
        n=5
        break
    
    a=L(tyAnd)
    if(n==1):
      a.t=tyAnd  
    if(n==2):
      a.t=tyOr  
    if(n==3):
      a.t=tyNot
    if(n==4):
      a.t=tyIn
    if(n==5):
      a.t=tyOut
      
    a.x=160-c.x
    a.y=111-c.y
  
  if(keydown(KEY_SQUARE)):
    slF=sl
  if(keydown(KEY_SQRT)):
    slT=sl
  
  if(keydown(KEY_RIGHT)):
    c.x-=5
    sl.x+=5*move
    m=True
  if(keydown(KEY_LEFT)):
    c.x+=5
    sl.x-=5*move
    m=True
  if(keydown(KEY_UP)):
    c.y+=5
    sl.y-=5*move
    m=True
  if(keydown(KEY_DOWN)):
    c.y-=5
    sl.y+=5*move
    m=True
  
  if(keydown(KEY_BACKSPACE)):
    m=True
    getl()[0].e=False
    del p[getl()[1]]
    sleep(0.5)
  
  if(move==0 and m):
    sl=getl()[0]
  
  if(m):
    fill_rect(0,0,320,240,[248,252,248])
  
  for i in p:
    i.update()
    i.draw()
  fill_rect(160-1,111-1,2,2,[0,0,248])
