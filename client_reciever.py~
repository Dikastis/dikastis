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


HOST = '192.168.43.165'
#HOST = ''
PORT = 4455

def reciever(soc):
    #reciving 
    data = soc.recv(10000)

    #writing to file
    f = open('notifications.txt','a+')
    f.write(data + "\n")
    f.close()

    data = data.split('$$$')
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

    reciever(soc)


socRecveiver = socket.socket()
print "thread working"
socRecveiver.connect((HOST , PORT))
socRecveiver.send('1001') #11 refers to client reciever type
response = socRecveiver.recv(100)
if response == "3000": # 101 refers ok
    socRecveiver.send("3001") # 102 refers ready to recieve data
    reciever(socRecveiver)
else:
    #handle error or show box
    pass
