import matplotlib.pyplot as plt
from numpy.random import random

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
tempsHigh = [33,41,45,30,38,33,43,55,59,63,62,39,53,42,42,36,36,45,49,60,68,69,70,67,49,37,44,40,55,66,44]
tempsLow = [15,12,28,19,18,22,11,32,25,48,32,21,18,24,18,26,31,30,21,24,29,46,47,49,34,31,26,32,22,44,25]


ax=plt.subplot()
ax.scatter(tempsHigh, days, cmap=plt.cm.plasma, s=100, label="High temp")
ax.scatter(tempsLow, days, cmap=plt.cm.plasma, s=100, label="Low temp")

plt.xlabel('Days')
plt.ylabel('Temp')
plt.title('TC Michigan Tempatures in March 2021')
plt.legend(loc='lower center', ncol=2, fontsize=8)
plt.grid()
plt.show()


