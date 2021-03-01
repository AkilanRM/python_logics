def timeInWords(h,m):
    num_dict={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}
    x=["quarter","half","minute","minutes","past","to"]
    for i in range(1,13):
        if(i==h):
            val=num_dict[i]
            val2=num_dict[i+1]
    
    for key,values in num_dict.items():
        if m not in num_dict.keys():
            if(m==1):
                res=val1+" "+x[2]+" "+x[4]+" "+val
                return res
            elif(m==30):
                res=x[1]+" "+x[4]+" "+val
                return res
            elif(m==45):
                res= x[0]+" "+x[5]+" "+val2
                return res
            elif(m==0):
                res=val+" o' clock"
                return res
            
            elif(m==15):
                res=x[0]+" "+x[4]+" "+val
                return res
            elif(m>30):
                if(m<40):
                    y=str(60-m)
                else:
                    y=(60-m)
            else:
                y=str(m)
            if(type(y)==str):
                val1=(num_dict[20]+num_dict[int(y[1])])
            else:
                val1=num_dict[y]
            if(m<30)and (m>20):
                y=str(m)
                val1=(num_dict[20]+num_dict[int(y[1])])
            
        else:          
            val1=num_dict[m]
            
        if(m<30):
            res=val1+" "+x[3]+" "+x[4]+" "+val
            return res
        else :
            res=val1+" "+x[3]+" "+x[5]+" "+val2
            return res
            
                



time=(input().split())
h=int(time[0])
m=int(time[1])
result=timeInWords(h,m)
print(result)
