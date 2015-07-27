#!/usr/bin/python

### Bjorn Pieper, End of july 2015
### This will process the .csv files produced by the MARVIN software containing the measurements
### of the individual objects. It will produce a single output file for further analysis. 

from os import listdir
from os.path import isfile, join
import re

path = "/home/bpuser/server/home/x-perimentz/common_garden/spring2015/Seed_Mass/Field_C_rco/"

## csv files in directory
files = [ x for x in listdir(path) if re.search('\.csv', x) and isfile(join(path, x)) ]

## Deal with German-style Windows csv to produce a clean list of values
line1 = True
for file in files:
    with open(path + file) as line:
        
        if line1 == True:
            header = [ x.strip('\r\n') for x in line.readline().split(';') ]
            with open('indiv_seeds_processed.tbl', 'wb') as output:
                output.write('\t'.join(['sample', 'block', 'column', 'row']) + '\t' + '\t'.join([ x.strip('"') for x in [re.sub('\s', '_', x) for x in header[1:len(header)]] ]) + '\n')
            line1 = False
        else:
            line.next()
        data = [[ re.sub(',', '.', x.strip('\r\n')) for x in y.split(';')] for y in line ] 
        sample = [ x.strip('.csv') for x in file.split(' ') ]
        
        with open('indiv_seeds_processed.tbl', 'ab') as output:
            for out in data:
                output.write('\t'.join(sample[0:2]) + '\t' + '\t'.join(sample[2].split('.')) + '\t' + '\t'.join(out[1:len(out)]) + '\n')
