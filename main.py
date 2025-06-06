import sys
import pandas as pd
import re

droppedfile = sys.argv[1]

dropper = [
    "Caller", 
    "Original CLI", 
    "CLI", 
    "Original CLD", 
    "Country", 
    "Description", 
    "Setup Time", 
    "Connect Time", 
    "Disconnect Time", 
    "Duration, sec", 
    "Cost", 
    "Currency", 
    "Result",
    "Remote IP",
    "LRN Original CLD",
    "LRN CLD",
    "Area Name",
    "Release Source",
    "Error Message"
]

s = str(droppedfile)
res = re.sub(r"Call_Records_from_(\d{4}-\d{2}-\d{2})_\d{2}_\d{2}_\d{2}_to_.*$", r"CallRecords\1", s)

df = pd.read_csv(droppedfile)
df = df.drop(columns=dropper)
df = df[df["Billing Prefix"] != "onnet_in"]
df = df[df["Billed Duration, sec"] >= 30]

df.to_csv(f"{res}.csv", index=False)
