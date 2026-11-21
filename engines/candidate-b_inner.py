import json,os,sys,urllib.request as U
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit()
def post(p,d):
 r=U.Request(E+p,data=json.dumps(d).encode(),headers={"content-type":"application/json"})
 try:return json.load(U.urlopen(r))
 except Exception as x:sys.exit(str(x))
V=(0,100,320,330,500,900,0)
def pv(p,s):
 t=(p-1)%6+1;f=s&7;r=s>>4;r=r if p<7 else 7-r
 c=7-abs(2*f-7)-abs(2*r-7)
 v=V[t]+(0,(r-1)*8+c+7,c*3,c*2,r*3,c,-r*8)[t]
 return v if p<7 else -v
TY=[0]+[(i-1)%6+1 for i in range(1,13)]
SQ=[s for s in range(128)if not s&0x88]
PT=[[pv(p,s)for s in range(128)]for p in range(13)]
ND=(14,18,31,33,-14,-18,-31,-33);KD=(1,-1,15,-15,16,-16,17,-17)
RD=(1,-1,16,-16);BD=(15,-15,17,-17);QD=RD+BD
b=[0]*128;turn=1;ep=-1;cs=0;EV=0;nodes=0;CAP=25000;TT={};K=[0]*64;path=[]
def key():return bytes(b)
def load(f):
 global b,turn,ep,cs,EV,path
 q=f.split();b=[0]*128
 for i,row in enumerate(q[0].split('/')):
  r=16*(7-i);j=0
  for ch in row:
   if ch.isdigit():j+=int(ch)
   else:
    x=' PNBRQK'.index(ch.upper());b[r+j]=x if ch.isupper()else x+6;j+=1
 turn=1 if q[1]=='w'else-1
 cs=(1 if'K'in q[2]else 0)|(2 if'Q'in q[2]else 0)|(4 if'k'in q[2]else 0)|(8 if'q'in q[2]else 0)
 ep=-1 if q[3]=='-'else 16*(int(q[3][1])-1)+ord(q[3][0])-97
 EV=sum(PT[p][s]for s,p in enumerate(b)if p);path=[key()]
def atk(s,c):
 w=c>0
 for d in((-15,-17)if w else(15,17)):
  t=s+d
  if t>=0 and not t&0x88 and b[t]==(1 if w else 7):return 1
 for ds,o in((ND,2),(KD,6)):
  for d in ds:
   t=s+d
   if t>=0 and not t&0x88 and b[t]==(o if w else o+6):return 1
 for ds,o in((RD,4),(BD,3)):
  for d in ds:
   t=s+d
   while t>=0 and not t&0x88:
    q=b[t]
    if q:
     if q==(o if w else o+6)or q==(5 if w else 11):return 1
     break
    t+=d
 return 0
def chk(c):return atk(b.index(6 if c>0 else 12),-c)
def gen():
 m=[]
 for fr in SQ:
  p=b[fr]
  if not p or(p>6)!=(turn<0):continue
  t=TY[p]
  if t==1:
   d=16*turn;to=fr+d
   if not to&0x88 and not b[to]:
    if to>>4 in(0,7):
     for x in(5,4,3,2):m.append((fr,to,x if turn>0 else x+6))
    else:m.append((fr,to,0))
    to2=fr+2*d
    if not to2&0x88 and not b[to2]and fr>>4 in(1,6):m.append((fr,to2,0))
   for z in(d-1,d+1):
    to=fr+z
    if to&0x88:continue
    q=b[to]
    if q and(q>6)!=(turn<0):
     if to>>4 in(0,7):
      for x in(5,4,3,2):m.append((fr,to,x if turn>0 else x+6))
     else:m.append((fr,to,0))
    elif to==ep:m.append((fr,to,0))
  elif t==2:
   for d in ND:
    to=fr+d
    if not to&0x88 and(not b[to]or(b[to]>6)!=(turn<0)):m.append((fr,to,0))
  elif t in(3,4,5):
   for d in(BD if t==3 else RD if t==4 else QD):
    to=fr+d
    while not to&0x88:
     if not b[to]:m.append((fr,to,0))
     else:
      if(b[to]>6)!=(turn<0):m.append((fr,to,0))
      break
     to+=d
  else:
   for d in KD:
    to=fr+d
    if not to&0x88 and(not b[to]or(b[to]>6)!=(turn<0)):m.append((fr,to,0))
   if turn>0 and fr==4 and not atk(4,-1):
    if cs&1 and not b[5]and not b[6]and not atk(5,-1)and not atk(6,-1):m.append((4,6,0))
    if cs&2 and not b[3]and not b[2]and not b[1]and not atk(3,-1)and not atk(2,-1):m.append((4,2,0))
   if turn<0 and fr==116 and not atk(116,1):
    if cs&4 and not b[117]and not b[118]and not atk(117,1)and not atk(118,1):m.append((116,118,0))
    if cs&8 and not b[115]and not b[114]and not b[113]and not atk(115,1)and not atk(114,1):m.append((116,114,0))
 return m
def legal():
 r=[]
 for m in gen():
  u=move(*m)
  if not chk(-turn):r.append(m)
  unmove(u)
 return r
def move(fr,to,pr=0):
 global b,turn,ep,cs,EV
 p=b[fr];cap=b[to];cp=to;e0=ep;s0=cs;EV-=PT[p][fr]
 if not cap and TY[p]==1 and to==ep and abs(to-fr)in(15,17):
  cp=to-16*turn;cap=b[cp]
 if cap:EV-=PT[cap][cp];b[cp]=0
 np=pr or p;b[fr]=0;b[to]=np;EV+=PT[np][to]
 if TY[p]==6 and abs(to-fr)==2:
  rf,rt=((7,5)if to==6 else(0,3)if to==2 else(119,117)if to==118 else(112,115))
  r0=b[rf];b[rt]=r0;b[rf]=0;EV+=PT[r0][rt]-PT[r0][rf]
 ep=(fr+to)//2 if TY[p]==1 and abs(to-fr)==32 else-1
 if fr==4:cs&=~3
 if fr==116:cs&=~12
 if fr==0 or to==0:cs&=~2
 if fr==7 or to==7:cs&=~1
 if fr==112 or to==112:cs&=~8
 if fr==119 or to==119:cs&=~4
 turn=-turn
 return(fr,to,p,cap,cp,e0,s0)
def unmove(u):
 global b,turn,ep,cs,EV
 fr,to,p,cap,cp,e0,s0=u;turn=-turn;ep=e0;cs=s0
 if TY[p]==6 and abs(to-fr)==2:
  rf,rt=((7,5)if to==6 else(0,3)if to==2 else(119,117)if to==118 else(112,115))
  r0=b[rt];b[rf]=r0;b[rt]=0;EV+=PT[r0][rf]-PT[r0][rt]
 np=b[to];EV+=PT[p][fr]-PT[np][to];b[to]=cap if cp==to else 0;b[fr]=p
 if cap:EV+=PT[cap][cp];b[cp]=cap
def ev():return(EV+(30 if b.count(3)>1 else 0)-(30 if b.count(9)>1 else 0))*turn
def ordered(ms,tt=None):
 def k(m):
  s=1000000 if m==tt else 0;q=b[m[1]]
  if q:s+=1000*V[TY[q]]-V[TY[b[m[0]]]]
  if m[2]:s+=1000*V[TY[m[2]]]
  if m in K:s+=900
  return-s
 return sorted(ms,key=k)
def qs(a,be,p):
 global nodes
 nodes+=1
 if nodes>CAP:raise TimeoutError
 if chk(turn):
  ms=legal()
  if not ms:return-30000+p
 else:
  x=ev()
  if x>=be:return be
  if x>a:a=x
  ms=[m for m in legal()if b[m[1]]or m[2]or(TY[b[m[0]]]==1 and m[1]==ep and abs(m[1]-m[0])in(15,17))]
 for m in ordered(ms):
  u=move(*m);v=-qs(-be,-a,p+1);unmove(u)
  if v>=be:return be
  if v>a:a=v
 return a
def sr(d,a,be,p):
 global nodes
 nodes+=1
 if nodes>CAP:raise TimeoutError
 k=key()
 if p and k in path:return 0
 if d<=0:return qs(a,be,p)
 tt=None;e=TT.get(k)
 if e:
  ed,esc,ef,em=e;tt=em
  if ed>=d:
   if ef==0:return esc
   if ef==1 and esc>=be:return esc
   if ef==-1 and esc<=a:return esc
 path.append(k);a0=a;ms=legal()
 if not ms:
  v=-30000+p if chk(turn)else 0;path.pop();return v
 best=-1000000;bm=None
 for m in ordered(ms,tt):
  u=move(*m);v=-sr(d-1,-be,-a,p+1);unmove(u)
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=be:K[p]=m;break
 path.pop();TT[k]=(d,best,0 if a0<best<be else 1 if best>=be else-1,bm)
 return best
def puci(s):
 fr=16*(int(s[1])-1)+ord(s[0])-97;to=16*(int(s[3])-1)+ord(s[2])-97;pr=0
 if len(s)>4:
  ty=5-'qrbn'.find(s[4]);pr=ty if turn>0 else ty+6
 return fr,to,pr
def uci(m):
 fr,to,pr=m;s=chr(97+(fr&7))+str((fr>>4)+1)+chr(97+(to&7))+str((to>>4)+1)
 return s+('qrbn'[5-((pr-1)%6+1)]if pr else'')
def root(d,ms):
 a=-1000000;bm=ms[0]
 for m in ordered(ms,TT.get(key(),(0,0,0,None))[3]):
  u=move(*m);v=-sr(d-1,-1000000,-a,1);unmove(u)
  if v>a:a=v;bm=m
 return bm,a
def think(f,lm):
 global nodes,TT,K,path
 nodes=0;load(f);ms=[puci(x)for x in lm]
 if not ms:return''
 bm=ms[0];TT={};K=[0]*64
 for d in range(1,12):
  try:
   m,v=root(d,ms)
   if m:bm=m
   if abs(v)>29000:break
  except TimeoutError:break
 return uci(bm)
if __name__=="__main__":
 while True:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   m=think(g["fen"],g["legal_moves"])
   if m not in g["legal_moves"]:m=g["legal_moves"][0]
   g=post("/move",{"game":g["game"],"move":m})
