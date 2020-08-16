from Compiler import *
import Compiler
import os,datetime
import _thread
print("Swami# 1.6.1, type credits for more info")
def notepad(f):
    os.system("notepad.exe Programs/"+f)
    return
while 1:
    command=input(">>> ")
    if command== "exit":
        break
    elif command=="credits":
        print("Developed By ClackHack, inspired by his friend (You know who you are)")
    elif begin(command,"file "):
        f=command.replace("file ","")
        try:
            open("Programs/"+f,"r").read()
        except:
            open("Programs/"+f,"w").write("")
        _thread.start_new_thread(notepad,(f,))
        #os.system("notepad.exe Programs/"+f)
    elif begin(command,"run "):
        f = command.replace("run ","")
        try:
            code=open("Programs/"+f,"r").read()
            y=datetime.datetime.now()
            c=compile(code)
            x=datetime.datetime.now()
            if type(c) == error:
                print("",c,sep="\n")
            elif c==0:
                print(f"\nExecuted with zero errors in {(x-y).total_seconds()} seconds")
        except Exception as e:
            print("Could not find file, or fatal error...",e)
            try:
               print(Compiler._line,", Line: ",Compiler.linenum,sep="")
            except:
                pass
    elif command=="swami":
        code=""
        while 1:
            line=input("")
            code+= line+"\n"
            if line=="zoinks 0":
                break
        code=code.strip()
        try:
            y=datetime.datetime.now()
            c=compile(code)
            x=datetime.datetime.now()
            if type(c) == error:
                print("\n",c,sep="")
            elif c==0:
                print(f"\nExecuted with zero errors in {(x-y).total_seconds()} seconds")
        except Exception as e:
            print("Fatal error...",e)
            try:
                print(Compiler._line,", Line: ",Compiler.linenum,sep="")
            except:
                pass
    elif command=="programs":
        f=os.listdir("Programs")
        for p in f:
            print(p)
    elif begin(command,"delete"):
        f = command.replace("delete ","").strip()
        try:
            os.remove("Programs/"+f)
        except:
            print("The file you specified was not found...")
    elif command == "repl":
        print("Swami# REPL, type exit to exit REPL")
        while 1:
            code=input(". ")
            if code == "exit":
                break
            if begin(code, "if"):
                depth=1
                
                while 1:
                    c1 = input(".. ")
                    if c1 == "jeepers":
                        depth-=1
                    elif c1=="zoinks":
                        depth-=1
                    elif begin(c1,"loop"):
                        depth+=1
                    elif begin(c1,"if"):
                        depth+=1
                    code+="\n"+c1
                    if depth==0:
                        break
            elif begin(code, "loop"):
                depth=1
                while 1:
                    c1 = input(".. ")
                    if c1 == "jeepers":
                        depth-=1
                    elif c1=="zoinks":
                        depth-=1
                    elif begin(c1,"loop"):
                        depth+=1
                    elif begin(c1,"if"):
                        depth+=1
                    code+="\n"+c1
                    if depth==0:
                        break
            if begin(code, "def"):
                depth=1
                while 1:
                    c1 = input(".. ")
                    if c1 == "jeepers":
                        depth-=1
                    elif begin(c1,"zoinks"):
                        depth-=1
                    elif begin(c1,"loop"):
                        depth+=1
                    elif begin(c1,"if"):
                        depth+=1
                    code+="\n"+c1
                    if depth==0:
                        break
            code+="\nzoinks 0"
            try:
                c=compile(code)
                if type(c) == error:
                    print("\n",c,sep="")
            except Exception as e:
                print("Fatal error...",e)
                try:
                    print(Compiler._line,", Line: ",Compiler.linenum,sep="")
                except:
                    pass
    elif command=="help":
        print("Commands are file, run, swami, programs, delete, repl, and exit\nCheck the github page for syntax support")
    else:
        print("Unkown command...\ntype help for help... ")
print("Exiting...")
