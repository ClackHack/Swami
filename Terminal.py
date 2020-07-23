from Compiler import *
import os
print("Swami# 1.2, type credits for more info")

while 1:
    command=input(">>> ")
    if command== "exit":
        break
    elif command=="credits":
        print("Developed By Clay Hess 2020, inspired by Hayes Houseworth")
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
            c=compile(code)
            if type(c) == error:
                print("",c,sep="\n")
            elif c==0:
                print("\nExecuted with zero errors")
        except Exception as e:
            print("Could not find file, or fatal error...",e)
    elif command=="swami":
        code=""
        while 1:
            line=input("")
            code+= line+"\n"
            if line=="zoinks 0":
                break
        code=code.strip()
        try:
            c=compile(code)
            if type(c) == error:
                print("\n",c,sep="")
            elif c==0:
                print("\nExecuted with zero errors")
        except Exception as e:
            print("Fatal error...",e)
    
    else:
        print("Unkown command...\nCommands are file, run, swami ")
print("Exiting...")
