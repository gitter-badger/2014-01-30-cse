#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'))
parser.add_argument('outfile', type=argparse.FileType('w'))
args = parser.parse_args()

f = args.infile
thi = list()
tlo = list()

for line in f:
    try:
        thi.append(float(line[111:114])/10)
        tlo.append(float(line[180:190])/10)
    except:
        continue
f.close()

g = args.outfile
g.write(repr(sum(thi) / len(thi)) + '\t' + repr(sum(tlo) / len(tlo)))

