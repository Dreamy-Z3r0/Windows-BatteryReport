import matplotlib.pyplot as plt
import numpy as np

file = 'C:\\Users\\dohoang\\Desktop\\Monitor - Battery Information.csv'
fileContent = []
with open(file, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            f.close()
            break
        else:
            fileContent.append(line)

fileContent.pop(0)

xContent = []
yContent = []

dateInCheck = None
sumValue = 0
count = 0
dataCount = 0

for line in fileContent:
    temp = line.find(',')
    dateInCheck_line = line[0:temp]

    if dateInCheck_line != dateInCheck:
        if dateInCheck is not None:
            xContent.append(count)
            yContent.append(sumValue / dataCount)

            sumValue = 0
            dataCount = 0

        count += 1
        dateInCheck = dateInCheck_line

    temp = line.rfind(',')
    dateInCheck_line = line[temp+1:].strip('\n')

    sumValue += float(dateInCheck_line)
    dataCount += 1

xContent = np.array(xContent)
yContent = np.array(yContent)

plt.plot(xContent, yContent,
         marker = 'o',
         linestyle = 'dotted',
         color = 'r')
plt.ylim(0, 100)
plt.show()