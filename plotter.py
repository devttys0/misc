#!/usr/bin/env python

import sys
import csv
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

# Default settings
title = "Plot"
x_name = "x"
y_name = "y"
logarithmic = False
x = []
y = []

# Parse command line arguments
try:
    csv_file = sys.argv[1]
    f = open(csv_file, "r")
except KeyboardInterrupt as e:
    raise e
except Exception as e:
    print ("")
    print ("Usage: %s <csv input file> [--log]" % sys.argv[0])
    print ("")
    print ("Example CSV file:")
    print ("")
    print ('"This is the graph title","This is the X axis title","This is the Y axis title"')
    print ("1,10")
    print ("2,100")
    print ("3,1000")
    print ("4,10000")
    print ("")
    sys.exit(1)

if '--log' in sys.argv[1:]:
    logarithmic = True

# Parse specified CSV file
try:
    row_id = 0
    reader = csv.reader(f)

    for row in reader:
        row_id += 1

        if len(row) == 3:
            title = row[0]
            x_name = row[1]
            y_name = row[2]
        elif len(row) == 2:
            try:
                x.append(int(row[0]))
                y.append(int(row[1]))
            except ValueError as e:
                raise Exception("Invalid integer value in row %d: %s" % (row_id, str(row)))
        elif len(row) > 0:
            raise Exception("Invalid CSV entry in row %d: '%s'" % (row_id, str(row)))

except KeyboardInterrupt as e:
    raise e
except Exception as e:
    print ("Caught exception while processing CSV file '%s': %s" % (csv_file, str(e)))
    sys.exit(1)

f.close()

# Generate plot
plt = pg.plot(title=title, clear=True)
plt.plot(x, y, pen='y')
plt.setLabel('left', y_name)
plt.setLabel('bottom', x_name)
plt.setLogMode(logarithmic)

# Display plot
QtGui.QApplication.instance().exec_()
pg.exit()

