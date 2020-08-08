from Compiler import *
import Compiler
import os,datetime
print("Swami# 1.4.1, type credits for more info")

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
        os.system("notepad.exe Programs/"+f)
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
        os.remove("Programs/"+f)
    
    else:
        print("Unkown command...\nCommands are file, run, swami, programs, delete, and exit... ")
print("Exiting...")
