import matplotlib.pyplot as plt

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Total annual openings', 'Opening due to transfer', 'Openings due to change', 'Numeric change', 'Projected employment', 'Base Year Employment'
numUsed = [3730, 2500, 150, 1520, 32940, 31420]
explode = (.1, 0, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('purple', 'green','royalblue','darkred','hotpink')

fig1, ax1 = plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct=autopct_format(numUsed), shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("2020 Construction Labors Michiagn")

plt.show()