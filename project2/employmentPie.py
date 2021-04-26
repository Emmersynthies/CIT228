import matplotlib.pyplot as plt

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Average Employment', 'Employment march 2021', 'Employment feb 2021', 'Last year', 'Net change month'
numUsed = [141162,174400,171500,177900,2900]
explode = (.1, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('purple', 'green','royalblue','hotpink','darkred')

fig1, ax1 = plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct=autopct_format(numUsed), shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Employment 2021")

plt.show()