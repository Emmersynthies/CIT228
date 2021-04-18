import matplotlib.pyplot as plt

cubed = []
value = [1, 2, 3, 4, 5]
for number in value:
    cubed.append(number*number*number)
ax1 = plt.subplot(1,2,1)    
ax1.plot(value,cubed)
plt.title("Cubed")
plt.xlabel("Values", fontsize=11)
plt.ylabel("Input", fontsize=11)
plt.grid() 

line = []
value2 = [1, 2, 3, 4, 5]
for number2 in value:
    cubed.append(number2**2)
ax2 = plt.subplot(1,2,2)  
plt.style.use("seaborn-dark-palette")
ax2.plot(value2,pow,color="red",lw="2",marker=">")
plt.title("numbers lined", color= "red", fontsize="13")
plt.xlabel("Second Values", fontsize=11)
plt.ylabel("Input", fontsize=11)
plt.grid() 

plt.suptitle("Graphs", c="purple",fontfamily="Comic Sans MS", fontsize="18")
plt.subplots_adjust(top=.8,wspace=1)
plt.show()
