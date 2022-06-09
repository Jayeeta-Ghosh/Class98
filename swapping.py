def swapFile1():
    data_a=input("Enter the file name")
    data_a=open(data_a)
    with open(data_a,'r') as a:
    data_a=a.read()

def swapFile2():
    fo=input("Enter the file name")
    file2=open(fo)
    with open(file2,'r') as b:
    data_b=b.read()   

def swapFile3():
  with open(file2,'w') as a:
      a.write(data_b)
   
def swapFile4():   
   with open(file2,'w') as a:    
        a.write(data_a)

swapFile1()
swapFile2()
swapFile3()
swapFile4()        

        