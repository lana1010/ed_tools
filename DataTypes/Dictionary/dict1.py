## Assuming the input data is stored in a list of strings, 
## with each string representing a line in the format "ip - timestamp - value - description", 
## you can use the following code to calculate the sum of the third column for each IP address:
##

# version 1 with regular expression
import re
res={}

with open("ip.txt","r") as file:
  for line in file:
    line=line.strip()
    match=re.search(r"^(\S+) - \S+ - (\d+)",line)
    print(match)
    res[match.group(1)]=res.get(match.group(1),0) + int(match.group(2))
    print(res)
    
  for ip,s in res.items():
    print (ip + " : " + str(s) + "KB")
 
 
# version 2 with strings and dicrionary    
sums={}

with open("ip.txt","r") as file:
  for line in file:
    parts=line.split("-")
    ip=parts[0]
    value=int(parts[2])
    if ip in sums:
      sums[ip] += value
    else:
      sums[ip] = value
      
for ip,sum in sums.items():
  print(f"{ip}: {sum}")