import datetime

'''this Convert year form S.E. to B.E. '''
def Conyear():
    y=datetime.datetime.now()
    yto=y.year+543                                       #Convert year S.E. to B.E. by +543 of year
    return str(yto)[2:4]                                 #Substring by slicing string [start:end]

'''this is ID-group by 099 ''' 
def Idgroup():
    gid='99'
    #g="099"                                             #get number 99
    return gid.zfill(3)                                  #string method [.zfill()] add 0 at begin of string

'''This is gennerate student-id 0001-1000 by string and convert this to integer and get function chack condition '''
def Genner(gx):
    numstart = 0
     
    for i in range(gx):
        numstart=numstart+1
        id=Conyear()+Idgroup()+str(numstart).zfill(4)    #sum all number form string can change to integer
        if int(i)%2==0:                                  #Chack condition for proposition
            #print(id,end="")
            ifs=(int(id)%5)*2+1
            print(id+str(ifs))
        else:
            #print(id,end="")
            els=(int(id)%5)*2
            print(id+str(els))    
Genner(1000)       