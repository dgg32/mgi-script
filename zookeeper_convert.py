import sys
import pandas as pd


inputfile = sys.argv[1]
outputfile = f"{inputfile.replace('.xlsx', '_converted.xlsx')}"

df = pd.read_excel(inputfile)

df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])

df.to_excel(outputfile)