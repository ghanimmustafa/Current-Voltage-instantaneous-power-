# By: Mustafa Ghanim


#Loading data to the program:

current=[];voltage=[];import numpy as np;import pylab as py;from math import sqrt as sq 
with open("rawdata.txt") as DATA:
    data_=[line.split()for line in DATA if not line.isspace()]
    data=np.array(data_)
    t=data[1:,0]
    I=data[1:,1]
    v=data[1:,2]
#Making a function that determines the sign of binary values:            
    def signed_value(s):
        if s[0] == '1':
            s = "-"+s[1:] 
        return int(s,base=2)
#Forming lists of current,voltage,and instantaneous power decimal values:
    for i in I:
        d_c=signed_value(i)
        current.append(d_c)
    for j in v:
        d_v=signed_value(j)
        voltage.append(d_v)
    power=np.multiply(current,voltage)
    print ("Time Values:",t)
    print("Current Values:",current)
    print("Voltage Values:",voltage)
    print("Instantaneous Power Values",power)
#Calculating the average,peak ,and rms values of the current and voltage:
    current_avg=np.mean(current);voltage_avg=np.mean(voltage)
    current_peakvalue=max(current);voltage_peakvalue=max(voltage)
    def rms(x):
        return sq(np.mean(np.square(x)))
    current_rms=rms(current);voltage_rms=rms(voltage)
    print(" The average value of current is %5.4f "%current_avg)
    print("The average value of voltage is %5.4f "%voltage_avg)
    print("The absoulte peak value of current is %5.4f "%current_peakvalue)
    print("The absoulte peak value of voltage is %5.4f "%voltage_peakvalue)
    print("The rms value of current is %5.4f "%current_rms)
    print("The rms value of voltage is %5.4f "%voltage_rms)

#Plotting the asked graphs in the same window:
    py.subplot(3,1,1)
    py.plot(t,current,"-r",linewidth=2)
    py.grid()
    py.xlabel("Time",fontsize=10);py.ylabel("Current")
    py.subplot(3,1,2)
    py.plot(t,voltage,"-b",linewidth=2)
    py.grid()
    py.xlabel("Time",fontsize=10);py.ylabel("Voltage")
    py.subplot(3,1,3)
    py.plot(t,power,"-y",linewidth=2)
    py.grid()
    py.xlabel("Time",fontsize=10);py.ylabel("Instantaneous Power ")   
    py.show()
#Importing csv and pandas libraries and writing the decimal values of time, current,voltage,and power to
#a text file called "powdata.txt". Note: Pandas library needs to be downloaded to be able to work correctly. 
    import csv;import pandas
    df=pandas.DataFrame({"time(s)":t,"Voltage(V)":voltage,"Current(A)":current,"Power(W)":power})
    df.to_csv('powdata.txt',sep='\t',index=False)
    
        
            
    
    
    
