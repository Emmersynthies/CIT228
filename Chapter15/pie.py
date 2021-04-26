import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numUsed = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('purple', 'green','lightblue','red','pink')

fig1, ax1 = plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Most used Image format")

plt.show()