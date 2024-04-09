from tkinter import *

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.dates as mdates

import datetime as dt

class Plot:
    def __init__(self, title="Battery Monitor", geometry=None, configFile="config.xml"):
        self.configFile = configFile
        self.fetch_plot_data()

        self.appTitle = title
        self.appGeometry = geometry

        # Initialise the plotting app
        self.app = Tk()
        self.app.title(self.appTitle)

        if self.appGeometry is not None:
            self.app.geometry(self.appGeometry)

        for field in self.fieldsOfInterest:
            self.canva(field)

        # Main loop
        self.app.mainloop()

    def fetch_plot_data(self):
        from parse_xml import ParseXML

        # Fetch data file
        dataFile = ParseXML(self.configFile)
        dataFile = dataFile.contentsAsDict

        self.dataFile = dataFile['config']['data_dir'] + '\\' + dataFile['config']['data_file']
        self.fieldsOfInterest = dataFile['config']['data_of_interest']['field']

        if type([]) != type(self.fieldsOfInterest):
            self.fieldsOfInterest = [self.fieldsOfInterest]

        if 'Remaining Capacity (%)' in self.fieldsOfInterest:
            self.fieldsOfInterest.append('Mode of Operation')

        # Fetch data
        self.fileContents = {}
        indicesOfInterest = []
        with open(self.dataFile, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    f.close()
                    break
                else:
                    line = line.strip('\n').split(',')
                    if [] == indicesOfInterest:
                        for field in self.fieldsOfInterest:
                            indicesOfInterest.append(line.index(field))
                            self.fileContents.update({field:[]})
                    else:
                        for index, field in enumerate(self.fieldsOfInterest):
                            temp = [line[0], line[1], line[indicesOfInterest[index]]]
                            self.fileContents[field].append(temp)   

        if 'Battery Health (%)' in self.fieldsOfInterest:
            temp = []
            dateInCheck = None
            tempSum = 0
            tempCount = 0
            for listValue in self.fileContents['Battery Health (%)']:
                entryDate = listValue[0]
                if entryDate != dateInCheck:
                    if dateInCheck is not None:
                        temp.append([dateInCheck, tempSum/tempCount])

                    dateInCheck = entryDate
                    tempSum = 0
                    tempCount = 0

                tempSum += float(listValue[2])
                tempCount += 1
            self.fileContents['Battery Health (%)'] = temp

    def canva(self, field):
        plotData = self.fileContents[field]
        yContent = [entry[-1] for entry in plotData]

        xContent_temp = [entry[0] for entry in plotData]
        xContent = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in xContent_temp]

        fig = Figure()
        plot_canva = fig.add_subplot(111)

        if 'Battery Health (%)' == field:
            plot_canva.plot(xContent, yContent,
                            marker = 'o',
                            linestyle = 'dotted')
            plot_canva.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            plot_canva.xaxis.set_major_locator(mdates.DayLocator(interval=7))
            plot_canva.tick_params(axis='x',labelrotation=30)

        fig.suptitle(field)

        if '%' in field:
            plot_canva.set_ylim([0, 100])

        canvas = FigureCanvasTkAgg(fig, master = self.app) 
        canvas.draw()

        canvas.get_tk_widget().pack()

if __name__ == '__main__':
    testClass = Plot()