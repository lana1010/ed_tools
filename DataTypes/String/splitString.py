###########################################
#
# Split a string into a list of strings
# Replacement, string 
#
###########################################

record = "Lev Tolstoy*1828-8-28*1910-11-20"
fields = record.split("*")
print("Splitting the string")
print (fields)

born = fields[1].split("-")
print ("Lev Tolstoy was born ",born)

died = fields[2].split("-")
print ("Lev Tolstoy died ", died)

print ("Lev Tolstoy lived about ", int(died[0]) - int(born[0]), "years")

print ("His first novel '{0}' was published in {1}".format("Hard Times", 1854))
print("\n")


### replacement with str.format()
print ("Replacemant")
print ("{{{0}}} {1} ;-)".format("I'm in braces","I'm not")) #to include braces inside format, double them
print("\n")


### concatenate  a string and a number with str.format()
#1
conc = "{0}{1}".format("The amount due is $", 200)
print ("Concatenation, #1")
print (conc+"\n")

#2
x = "three"
s = "{0}{1}{2}"
s = s.format("The ", x, " tops")
print ("Concatenation, #2")
print (s+"\n") 

#3
aa = "The {who} was {0} last week".format(12, who = "boy")
print ("Concatenation, #3")
print (aa+"\n")

#4
stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
print ("Concatenation, #4")
aa = "We have {0[1]} and {0[2]} in stock".format(stock)
print (aa+"\n")

#5
d = dict(animal="elephant", weight=12000)
aa = "The {0[animal]} weighs {0[weight]} kg".format(d)
print ("Concatenation, #5")
print (aa+"\n")