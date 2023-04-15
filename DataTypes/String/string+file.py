# Use the file name mbox-short.txt as the file name
# Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence: 0.7002
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
#
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count=0
summ=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    pos=line.find(':')
    num=float(line[pos+1:])
    summ=summ+num

avg=summ/count
print ('Average spam confidence:', avg)