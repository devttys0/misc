#!/usr/bin/env python
# Normalizes the frequency (second CSV entry) for f-T curve data used by plotter.py.
import sys

def process_line(line):
    try:
        (temp, freq) = line.strip().split(',')
        return (int(temp), float(freq))
    except Exception as e:
        sys.stderr.write("Error processing line '%s' : %s\n" % (line, str(e)))
        sys.exit(1)

fp = open(sys.argv[1])

title = fp.readline()
(base_temp, base_freq) = process_line(fp.readline())
print title.strip()
print "%d,%1f" % (base_temp, 0)

for line in fp.readlines():
    line = line.strip()
    if line and not line.startswith('#'):
        (temp, freq) = process_line(line)
        print "%d,%1f" % (temp, freq-base_freq)
