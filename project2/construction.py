import matplotlib.pyplot as plt  
import numpy as np 
    
nonresidential = [789507,840564]
residential = [727420,600581]
total=[1516927,1441145]
periods=["Feb2021","Feb2020"]
barWidth=.25

br1 = np.arange(len(periods)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.xticks([r + barWidth for r in range(len(periods))],periods) 


# creating the bar plot 
plt.bar(br1, nonresidential, color ="purple", width=barWidth, label="Nonresidential") 
plt.bar(br2,residential, color="red",  width=barWidth, label="Residential")
plt.bar(br3,total, color="grey", width=barWidth,  label="Total Construction")
  
plt.ylabel("$$$") 
plt.xlabel("2020 vs 2021") 
plt.title("Construction between years") 
plt.legend(loc="best")
plt.show() 

