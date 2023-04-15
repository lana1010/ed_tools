#
# Use 2 files: vars.txt and data.txt
# Assign values from vars.txt to variables in data.txt
#


data_file = ("data.txt")
var_dict = dict()
data_dict = dict()

"""
mylist = [1, 2, 3]
mydict = {}
mydict['hello'] = mylist
mydict['world'] = [4,5,6]
print(mydict)
"""

var_file = open("vars.txt","r")
for line in var_file:
    line = line.strip().split("=")
    print (line)
    first = line[0]
    second = line[1]
    var_dict[first] = second
    
var_file.close()    
#print (var_dict["var1"])

data_file = open("data.txt","r")
output_file = open("output.txt","w")
for line in data_file:
    line = line.strip().split("=")
    print (line)
    first = line[0]
    if (first == 'var1'):
      data_dict[first] = var_dict["var1"]
    elif (first == 'var2'):
      data_dict[first] = var_dict["var2"] 
    elif (first == 'var3'):
      data_dict[first] = var_dict["var2"]
    else:
      print ("element is not present")

data_file.close() 

output_file = open("output.txt","w")
output_file.write(str(data_dict))
output_file.close()

      
          
print ("\n")          
print (var_dict)
print (data_dict)
