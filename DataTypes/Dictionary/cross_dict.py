# Combine two dictionaries having key of the first dictionary
# and value of the second dictionary
# Using loop + keys()

# initializing dictionaries
test_dict1 = {"Height" : 20, "Width" : 36, "Depth" : 100}
test_dict2 = {"Height2" : 200, "Width2" : 360, "Depth2" : 500}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# extracting keys and values
keys1 = list(test_dict1.keys())
vals2 = list(test_dict2.values())

# assigning new values
res = dict()
for idx in range(len(keys1)):
	res[keys1[idx]] = vals2[idx]
	
# printing result
print("Mapped dictionary : " + str(res))
