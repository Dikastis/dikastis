import socket
import tkMessageBox

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()
root.withdraw()


HOST = ''
#HOST = ''
<<<<<<< HEAD
PORT = 4464
=======
PORT = 4466
>>>>>>> eab0a8724bfbd9dbe0f58548a09ec0600d4e4a5b

def reciever(soc):

    while 1:
        #reciving 
        data = soc.recv(100000)

        #writing to file
        f = open('notifications.txt','a+')
        f.write(data + "\n")
        f.close()

        data = data.split('$$$')
        try:
            if data[0] == "broadcast":
                tkMessageBox.showinfo( data[0], data[1] )
                print data
                soc.send("3002")
            elif data[0] == "result":
                tkMessageBox.showinfo( data[0], data[1] )
                print data
                soc.send("3002")
            else:
                tkMessageBox.showinfo( data[0], data[1] )
                soc.send("3002")
        except:
            soc.send("3002")




f=open('login_id.txt','r')
user_id = f.read()
f.close()

socRecveiver = socket.socket()
print "thread working"
socRecveiver.connect((HOST , PORT))
socRecveiver.send('1001') #11 refers to client reciever type
response = socRecveiver.recv(100)
if response == "3002": # 101 refers ok
    socRecveiver.send(str(user_id)) # 102 refers ready to recieve data
    reciever(socRecveiver)
else:
    #handle error or show box
    pass




