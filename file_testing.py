with open("things.txt","w") as f:
    for i in xrange(10):
        f.write("This is my favorite number %d, for the next milisecond." % i)
    
