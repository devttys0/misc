#!/usr/bin/env python

import re
import sys
import csv
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

# Default settings
title = "Plot"
x_name = "x"
y_name = "y"
x_units = ""
y_units = ""
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
    print ("Usage: %s <csv input file>" % sys.argv[0])
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

# Parse specified CSV file
try:
    row_id = 0
    reader = csv.reader(f)
    units = re.compile(r'\((.+?)\)', flags=re.DOTALL)

    for row in reader:
        row_id += 1

        if len(row) == 3:
            title = row[0]
            x_name = row[1]
            y_name = row[2]

            try:
                x_units = units.search(x_name).groups()[0]
                x_name = x_name.replace("(%s)" % x_units, "")
            except Exception:
                pass

            try:
                y_units = units.search(y_name).groups()[0]
                y_name = y_name.replace("(%s)" % y_units, "")
            except Exception:
                pass
        elif len(row) == 2:
            try:
                x.append(float(row[0]))
                y.append(float(row[1]))
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
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
plt = pg.plot(title=title, clear=True)
plt.plot(x, y, pen=pg.mkPen('b', width=3))
plt.setLabel('left', y_name, units=y_units)
plt.setLabel('bottom', x_name, units=x_units)

# Display plot
QtGui.QApplication.instance().exec_()
pg.exit()

