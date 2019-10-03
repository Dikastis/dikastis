def get_data_from_main(s):    
    data = s.recv(100000)

    f = open('submission_sub.b','wb')
    f.write(data)
    f.close()
    print "data data_received"
    data_recieved=pickle.load(open('submission_sub.b','rb'))

    data_recieved.display()

    file_name = data_recieved.problem_code 

    f = open(file_name+".cpp",'w')
    f.write(data_recieved.problem_statement)
    f.close()

    submission_queue.enqueue(data_recieved)

    a=soldier.run("python checker.py "+file_name + " " + file_name )

    print "returned to sub server"
    file = open("log.json","r")
    data = file.read()
    file.close()
    s.send(data)
