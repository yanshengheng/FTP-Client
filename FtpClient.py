import sys
import ftplib
import getpass
import os
def LoginRequire():
    print "example: 'ftp example.com' to connect to server"
    cmd = raw_input(">")
    if cmd.isspace():
        print "command not found"
        return None
    elif "ftp" not in cmd:
        print "command not recognized"
        return None
    elif "ftp" in cmd:
        addr = cmd.split(" ")[1]
        if addr.isspace():
            print "server address is required"
            return None
        else:
            print "--------------------------"
            ftp = Connect(addr)
            return ftp
    else:
        print "error occured"
        return None
        
def Menu(ftp):
    if ftp == None:
        print "connection error, program exit"
        sys.exit()
    cmd = "true"
    while("exit" not in cmd):
        print "--------------------------"
        print "'ls' to list files on current folder"
        print "'get filename' to download file on current path"
        print "'upload local-filename' to upload file to server"
        print "'delete filename' to delete server file "
        print "'exit' to quit ftp connection" 
        print "--------------------------"
        cmd = raw_input(">")
        HandleUserCommand(ftp,cmd)

def HandleUserCommand(ftp,cmd):
    if cmd.isspace():
        print "command not found"
    elif "ls" in cmd:
        print "--------------------------"
        ftp.retrlines("LIST") 
        print "--------------------------"
    elif "exit" in cmd: 
        ftp.quit()
        print "Ok Bye."
    elif "get" in cmd:
        filename = cmd.split(" ")[1]
        if filename.isspace():
            print "filename is required"
        else:
            GetFile(ftp,filename)
            print "file downloaded."
    elif "upload" in cmd:
        file = cmd.split(" ")[1]
        Upload(ftp, file)
    elif "delete" in cmd:
        filename = cmd.split(" ")[1]
        ftp.delete(filename)
    else:
        print "command not found"

def Connect(server_ip):
    ftp = ftplib.FTP(server_ip)
    username = raw_input("username: ")
    password = getpass.getpass()
    ftp.login(username,password)
    ftp.set_pasv(False) #it works onw on my machine
    return ftp

def GetFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, "wb").write)
    except:
        print "Error: download file failed"

def Upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
def Delete(ftp, filename):
    pass
if __name__=="__main__":
    ftp = LoginRequire()
    Menu(ftp)
