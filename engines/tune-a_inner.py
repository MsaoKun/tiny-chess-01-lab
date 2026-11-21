import json,os,urllib.request as R
U=os.environ["MAKEFUN_ENV_URL"];CP=50000;X=40000;Y=29000
A=[0]*128;E=-1;N=0;T={};H=set();K=[0]*40
Z="pnbrqk";S1="abcdefgh";V=0,100,320,330,500,900,0;PH=0,0,1,1,2,4,0
M=(0,7,2,1,2,0,-8),(0,4,5,3,0,1,0)
O=(0,14,3,1,2,0,5),(0,2,4,3,0,1,6)
L=[i for i in range(120)if not i&136]
def TB(p):return[[V[t]+(i>>4)*p[0][t]+(3-abs(i%8-3))*p[1][t]for i in range(120)]for t in range(1,7)]
W=[[0]*120]+TB(M);G=[[0]*120]+TB(O)
A4=(15,17,-15,-17);B4=(1,-1,16,-16);K8=(1,17,16,15,-1,-17,-16,-15);J8=(18,33,31,14,-18,-33,-31,-14)
DV=(0,0,[(d,1)for d in J8],[(d,8)for d in A4],[(d,8)for d in B4],[(d,8)for d in A4+B4],[(d,1)for d in K8])
def sd(w,b):return json.load(R.urlopen(U+w,json.dumps(b).encode()))
def ld(f):
 global A,E
 A=[0]*128;r=7;c=0;w=f.split()
 for h in w[0]:
  if h=="/":r-=1;c=0
  elif h>"9":A[r*16+c]=(Z.find(h.lower())+1)*(1-2*(h>"Z"));c+=1
  else:c+=int(h)
 E=-1
 if w[3]>"-":E=(int(w[3][1])-1)*16+ord(w[3][0])-97
def at(x,s):
 for t in range(2,7):
  for d,n in DV[t]:
   q=x+d
   while not q&136:
    v=A[q]
    if v:
     if v*s>0 and abs(v)==t:return 1
     break
    if n<8:break
    q+=d
 for d in(15,17):
  q=x-d*s
  if not q&136 and A[q]==s:return 1
def P(m,f,q):m+=[(f,q,x)for x in(5,4,3,2)]if(q>>4)%7<1 else[(f,q,0)]
def gen(s,c=0):
 m=[]
 for f in L:
  p=A[f]
  if p*s<1:continue
  t=abs(p)
  if t==1:
   if not c:
    q=f+16*s
    if not q&136 and not A[q]:
     P(m,f,q)
     if f>>4==1+5*(s<0) and not A[q+16*s]:m.append((f,q+16*s,0))
   for d in(15,17):
    q=f+d*s
    if not q&136 and(A[q]*s<0 or q==E):P(m,f,q)
  else:
   for d,n in DV[t]:
    q=f+d
    while not q&136:
     v=A[q]
     if v:
      if v*s<0:m.append((f,q,0))
      break
     if not c:m.append((f,q,0))
     if n<8:break
     q+=d
   if t==6 and not c:
    h=4+112*(s<0);o=-s
    if A[h]==6*s and not at(h,o):
     if A[h+3]==4*s and not(A[h+1]or A[h+2]or at(h+1,o)):m+=[(h,h+2,0)]
     if A[h-4]==4*s and not(A[h-1]or A[h-2]or A[h-3]or at(h-1,o)):m+=[(h,h-2,0)]
 return m
def mk(m):
 global E
 f,t,p=m;p0=A[f];c=A[t];e=E;ep=rt=0
 A[f]=0
 if not c and abs(p0)==1 and f&7!=t&7:
  ep=t-16 if p0>0 else t+16;c=A[ep];A[ep]=0
 A[t]=p*(1-2*(p0<0))or p0
 if abs(p0)==6 and abs(t-f)==2:
  a=t+1 if t>f else t-2;b=t-1 if t>f else t+1
  A[b]=A[a];A[a]=0;rt=a,b
 E=-1
 if abs(p0)==1 and abs(t-f)==32:E=(f+t)//2
 return f,t,p0,c,e,ep,rt
def um(u):
 global E
 f,t,p0,c,e,ep,rt=u
 A[f]=p0;A[t]=c
 if ep:A[ep]=c;A[t]=0
 if rt:A[rt[0]]=A[rt[1]];A[rt[1]]=0
 E=e
def lg(s):
 o=[];k=A.index(6*s)
 for m in gen(s):
  u=mk(m)
  if not at(u[1]if abs(u[2])==6 else k,-s):o.append(m)
  um(u)
 return o
def ev(s):
 m=e=p=wc=bc=0;pw=[];rk=[];fw=[8]*10;fb=[-1]*10
 for i in L:
  q=A[i]
  if not q:continue
  t=abs(q);p+=PH[t];j=i if q>0 else i^112
  if t==1:
   r=i>>4;f=1+i%8;pw.append((q,i,j,f))
   if q>0:fw[f]=min(fw[f],r)
   else:fb[f]=max(fb[f],r)
  else:
   w=W[t][j];g=G[t][j]
   if q<0:w=-w;g=-g
   m+=w;e+=g
   if t==3:wc+=q>0;bc+=q<0
   elif t==4:rk.append((q,1+i%8))
 if wc>1:m+=30
 if bc>1:m-=30
 mx=[max(fb[f:f+3])for f in range(9)]
 mn=[min(fw[f:f+3])for f in range(9)]
 for q,f in rk:
  if q>0:m+=16 if fb[f]<0 else(8 if fw[f]==8 else 0)
  else:m-=16 if fw[f]==8 else(8 if fb[f]<0 else 0)
 for q,i,j,f in pw:
  r=i>>4;rr=j>>4;w=W[1][j];g=G[1][j]
  if q>0:ps=mx[f]<r
  else:ps=mn[f]>r
  if ps:
   b=rr*rr*4+10;w+=b;g+=b*2
  if q<0:w=-w;g=-g
  m+=w;e+=g
 for q,k in((1,A.index(6)),(-1,A.index(-6))):
  sg=q*16
  for d in(-1,0,1):
   x=k+sg+d
   if not x&136:
    if A[x]==q:m+=12*q
    x+=sg
    if not x&136 and A[x]==q:m+=7*q
 return(m*p+e*(24-p))//24*s
def od(m,o):return sorted(m,key=lambda x:-(x==o)*999-V[abs(A[x[1]])]*10)
def qs(s,a,b):
 global N
 N+=1
 assert N<CP
 k=A.index(6*s);c=at(k,-s)
 if not c:
  v=ev(s)
  if v>=b:return b
  if v>a:a=v
 ms=gen(s,not c);z=-X
 for m in od(ms,0):
  u=mk(m)
  if at(u[1]if abs(u[2])==6 else k,-s):um(u);continue
  v=-qs(-s,-b,-a);um(u)
  if v>z:
   z=v
   if v>a:
    a=v
    if a>=b:return b
 return-Y if z<-X and c else z
def ne(s,d,a,b,q):
 global N
 N+=1
 assert N<CP
 if d<1:return qs(s,a,b)
 k=s,E,tuple(A)
 if q>1 and k in H:return 0
 v=T.get(k)
 if v is not None:
  if v>=b:return b
  if v>a:a=v
 ms=lg(s)
 if not ms:return-Y+q
 z=-X
 for m in od(ms,K[q]):
  u=mk(m);v=-ne(-s,d-1,-b,-a,q+1);um(u)
  if v>z:z=v
  if v>a:
   a=v
   if a>=b:
    if not A[m[1]]:K[q]=m
    break
 if d>2:T[k]=z
 return z
def c(m):
 f,t,p=m
 return S1[f&7]+str(1+(f>>4))+S1[t&7]+str(1+(t>>4))+(Z[p-1]if p else"")
def best(fen,lm):
 global A,E,N
 ld(fen);s=-1+2*(fen.split()[1]=="w")
 ms=[m for m in lg(s)if c(m)in lm]
 if not ms:return lm[0]if lm else 0
 H.add((s,E,tuple(A)))
 N=0;bm=ms[0]
 for d in range(1,10):
  a=-X;cb=0
  try:
   for m in od(ms,bm):
    u=mk(m);rp=0
    if len(H)>1:
     for r in lg(-s):
      u2=mk(r);rp|=(s,E,tuple(A))in H;um(u2)
    v=-ne(-s,d-1,-X,-a,1)-40*rp;um(u)
    if v>a:a=v;cb=m
  except:break
  if cb:bm=cb
 return c(bm)
Q=0
while 1:
 g=sd("/game",{})
 if g["status"]=="done":break
 if g["game"]!=Q:Q=g["game"];H.clear()
 while g["status"]=="your_move":
  try:m=best(g["fen"],g["legal_moves"])
  except:m=g["legal_moves"][0]
  g=sd("/move",{"game":Q,"move":m})
