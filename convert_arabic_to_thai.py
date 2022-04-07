REP = {"0":"๐", "1":"๑", "2":"๒", "3":"๓", "4":"๔", "5":"๕", "6":"๖", "7":"๗", "8":"๘", "9":"๙"}

filename = "data.csv"
fileout = "out.csv"
output = ""
with open(filename, "r", encoding="utf-8") as f:
	for line in f:
		for chr in REP:
			line = line.replace(chr, REP[chr]) 
		output += line

with open(fileout, "w", encoding="utf-8") as f:
	f.write(output)