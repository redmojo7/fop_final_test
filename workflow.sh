#!/bin/bash
#  gets files from the web/Internet
wget --user-agent="Mozilla"  http://www.bom.gov.au/climate/dwo/202202/text/IDCJDW6111.20202.csv
#  reads through data file and prints out those including the string "2019-02-" – redirect output to data.csv
grep "2022-02-" IDCJDW6111.202202.csv > data.csv
# - reads through data.csv and prints fields 3,4,11 & 17,
#   using "," as the field separator (-F ",")
# - counts fields from 1
# - redirects output to data4.csv
awk -F"," '{print $3, $4, $11, $17}' data.csv > data4.csv
# - runs gnuplot with the plotting commands in plotcmd.txt
gnuplot -p plotcmd.txt
