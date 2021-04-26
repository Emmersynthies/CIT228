import matplotlib.pyplot as plt  
    
wage = [15.22,17.16,19.65,22.14]
periods=["1-4","5-9","10-19","20"]

plt.barh(periods, wage, color ='red') 
  
plt.xlabel("Hourly wage") 
plt.ylabel("Years of experience") 
plt.title("Construction wages") 
plt.show() 