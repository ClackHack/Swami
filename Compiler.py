import math,random,re
global output
global in_if
comp=compile
variables={"args":[]}
functions={}
def split(s,d):
    out=[]
    current=""
    for i in s:
      if i in d:
        if current:
          out.append(current)
        current=""
      else:
          current+=i
    if current:
      out.append(current)
    return out
def begin(s,r):
  return s[:len(r)]==r
class error:
  def __init__(self,line,l,t,msg):
    self.line=line
    self.l=l
    self.t=t
    self.msg=msg
    self.child=None
  def __str__(self) :
    if self.child:
      return f"{self.t} error at line {self.line}:\n {self.msg}\n{self.l}\n"+self.child.__str__()
    else:
      return f"{self.t} error at line {self.line}:\n {self.msg}\n{self.l}"
  def addChild(self,error):
    self.child=error
class pyFunction:
  def __init__(self,code):
    self.code=code
    #print(type(code))
  def run(self,args,out=""):
    #print("args : ",args,"end")
    #print("debug")
    #print("running")
    
    #global output
    #print(args
    
    try:
      #raise Exception
      if args:
        x=self.code(args)
        
      else:
      #print("debug 1")
        x=self.code()
      if out:
        variables[out]=x
    except Exception as e:
        print(e)
        return error('Undefined','Internal Function','Runtime','')
class swamiFunction:
    def __init__(self,code):
        self.code=code
    def run(self,args,out=""):
        if out=="count":
                  print("here")
        variables["args"]=args
        e=compile(self.code)
        #print("swami",e)
        if error == type(e):
            return e
        else:
            if out:
              
              variables[out]=e
def anon(x):
    for q in x:
        print(q,end="")

functions["see"]=pyFunction(anon)
functions["index"]=pyFunction(lambda x: x[0][x[1]])
functions['bool']=pyFunction(lambda x:bool(x[0]))
functions['int']=pyFunction(lambda x:int(x[0]))
functions['str']=pyFunction(lambda x:str(x[0]))
functions['float']=pyFunction(lambda x:float(x[0]))
functions['list']=pyFunction(lambda x:list(x[0]))
functions['vars']=pyFunction(lambda:[print(p+" : "+str(q)) for p,q in variables.items()])
functions['functions']=pyFunction(lambda:[print(p) for p in functions.keys()])
functions['random'] = pyFunction(lambda x: random.randint(x[0],x[1]))
functions['<='] = pyFunction(lambda x: x[0]<=x[1])
functions['>='] = pyFunction(lambda x: x[0]>=x[1])
functions['<'] = pyFunction(lambda x: x[0]<x[1])
functions['>'] = pyFunction(lambda x: x[0]>x[1])
functions['=='] = pyFunction(lambda x: x[0]==x[1])
functions['!='] = pyFunction(lambda x: x[0]!=x[1])
functions["add"] = pyFunction(lambda x: x[0]+x[1])
functions["power"] = pyFunction(lambda x: x[0]**x[1])
functions["subtract"] = pyFunction(lambda x: x[0]-x[1])
functions["multiply"] = pyFunction(lambda x: x[0]*x[1])
functions["divide"] = pyFunction(lambda x: x[0]/x[1])
functions["input"] = pyFunction(lambda x: input(str(x[0])))
functions["not"] = pyFunction(lambda x: not x[0])
functions["and"] = pyFunction(lambda x: not x[0] and x[1])
functions["or"] = pyFunction(lambda x: not x[0] or x[1])
functions["len"]=pyFunction(lambda x: len(x[0]))
functions["append"]=pyFunction(lambda x: x[0].append(x[1]))
def compile(code):
  global in_if
  global activated
  global looplines
  looplines = 0
  in_if=False
  activated=False
  output=""
  global variables
  #output=""
  lines = code.split("\n")
  infunc=False
  function=""
  name=""
  l=[]
  depth=0
  global linenum
  inif=False
  for i in lines:
    #print("r")
    #linenum=i
    global _line
    if depth>0:
        #print("Function")
        function+=i+"\n"
        if begin(i,"if"):
            #print("inif")
            inif=True
            continue
        if inif:
            if begin(i,"jeepers"):
                #print("outif")
                inif=False
                continue
            continue
        elif begin(i,"loop"):
            depth+=1
        elif begin(i,"zoinks"):
            #print(depth)
            depth-=1
        
        if depth==0:
            #print("Func Created")
            functions[name]=swamiFunction(function.strip('\n'))
            #depth+=1
    elif begin(i,"def"):
      #print("function started")
      name=i.replace("def ","")
      depth+=1
    else:
        l.append(i)
  lines=l
  #print("lines",lines)
  for i in range(len(lines)):
    linenum=i
    ran=False
    line=lines[i]
    _line=lines[i]
    if looplines>0:
        looplines-=1
        continue
    if begin(line,"#"):
        continue
    if in_if and not activated:
        if begin(line,"jeepers"):
            in_if=False
            activated=False
            continue
        else:
            continue
    if line.replace(" ","")=="":
      continue
    if begin(line,"like"):
      ran=True
      try:
        l = line.replace("like ","")#.replace(" ","")
        
        e=l.find("=")
        name=l[:e].strip()
        if name=="":
            return error(i+1,_line,"Name","Im not seeing a name")
        args=l[e+1:]
        #print(l[e+1:])
        #print(name)
        #value=eval(args)
        raise Exception
        
      except:
            pattern="|".join(("+","-","/","*",'not',"or","and"))
            
            v=re.split("|".join(("\+","-","/","\*",'not',"or","and")),args)
            #print(args,v)
            #print(eval(v[0]))
            for q in v:
                #code=comp(q,"<string>",'eval')
                
                try:
                  args=args.replace(q.strip(),str(variables[q.strip()]))
                  #print(q)
                except:
                  try:
                      #print("test")
                      #print(args)
                      #print("q",q)
                      #print(variables[q.strip()])
                      eval(q)
                      #print(variables[q.strip()])
                      #print(args)
                  except Exception as e:
                      #print(e.args)
                      print("debug num 2")
                      return error(i+1,_line,"Syntax","Scooby dooby do, you declared your variable incorrectly")
            try:  
               #print(args)
               value=eval(args)
            except Exception as e:
              print("debug")
              return error(i+1,_line,"Syntax","Scooby dooby do, you declared your variable incorrectly")
      finally:
        #print(value)
        variables[name]=value
        #print(value,variables)
    elif begin(line,"jeepers"):
        ran=True
        if in_if:
            
            in_if=False
            continue
    elif begin(line,"zoinks"):
        #print(line)
        ran=True
        
        l=line.replace("zoinks ","")
        try:
          v=re.split("|".join(("\+","-","/","\*",'not',"or","and")),l)
          #print(v)
          for q in v:
            try:
              #print(q,variables[q.strip()])
              l=l.replace(q.strip(),str(variables[q.strip()]))
              #print(l)
            except Exception as e:
              #print(e)
              try:
                eval(q)
                #print(eval(q))
              except:
                return error(i+1,_line,"Syntax","like zoinks scoob, your return doesnt make sense")
        except:
          pass
          
        finally:
            try:
                #print(l,eval(l))
                return eval(l)
            except:
                return error(i+1,_line,"Syntax","like zoinks scoob, your return doesnt make sense")

        
    elif begin(line,"if"):
        ran=True
        l = line.replace("if ","")
        val = variables[l.strip()]
        in_if=True
        if val:
            activated=True
        else:
            activated=False
    elif begin(line,"loop"):
        ran=True
        l=line.replace("loop ","")
        val = variables[l.strip()]
        depth=1
        count=0
        text=""
        for q in lines[i+1:]:
            count+=1
            
            if begin(q,"if"):
                depth+=1
                
            elif begin(q,"zoinks"):
                depth-=1
            if depth==0:
                break
            text+=q+'\n'
        text=text.strip('\n')
        #print(text)
        while variables[l.strip()]:
            compile(text)
            
        looplines=count    
    for j,t in functions.items():
      if begin(line,j):
        ran=True
        line=line.replace(j,'')
        
        a=line.split(':')
        o=None
        if a[0]=="":
            a=[]
        if len(a)==0:
          o=t.run([])
         
        elif len(a)==1:
          args=a[0].replace(', ',',').split(',')
          ar=[]
          #print(args)
          for p in args:
              try:
                p=p.strip()
                #print(p,eval(p))
                if p=="endl":
                  arg="\n"
                else:
                  arg=variables[p]
                  
                  if arg==None:
                      raise TypeError
                #print(arg)
              except:
                try:
                  #print("variable",p)
                  arg=eval(p)
                  #print(arg)
                except Exception as e:
                    print(e)
                    return error(i+1,_line,"Runtime","What does this argument mean: "+p)
              finally:
                  try:
                    ar.append(arg)
                  except:
                    return error(i+1,_line,"Runtime","What does this argument mean: "+p)
          #print(ar)
          o=t.run(ar)
        elif len(a)==2:
          args=a[1].replace(', ',',').split(',')
          ar=[]
          #print("args",args,args[0])
          for p in args:
              try:
                p=p.strip()
                if p=="endl":
                  arg="\n"
                
                arg=variables[p]  
                #print("element",p,eval(p))
                
                #print(p,arg)
                if arg==None:
                  raise TypeError
                  #print(arg)
                #print(arg)
              except:
                #print("debug1")
                try:
                  #print(p)
                  arg=eval(p)
                  #print(arg)
                except:
                    #print("uh oh6")
                    return error(i+1,_line,"Runtime","What does this argument mean: "+p)
              finally:
                  try:
                    ar.append(arg)
                  except:
                    return error(i+1,_line,"Runtime","What does this argument mean: "+p)
          #print(ar)
          o=t.run(ar,out=a[0].strip())
          #print(ar)
          #print(o)
        if type(o)==error:
          o.addChild(error(i+1,_line,"Runtime","Invalid function call"))
          return o
    if not ran:
        return error(i+1,_line,"Syntax","I cant understand this line:")
        
    #print(i+1,ran)
        
  if output:
    return output
if __name__ == "__main__":
    
    code='''see "hello world!"
zoinks 0
'''
    o=compile(code)
    if o!=None:
        print("\n",o,sep="")
