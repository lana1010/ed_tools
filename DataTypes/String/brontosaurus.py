## Parsing string
## Count the sum of entries for each letter in a string

word = 'Before Pence delivered that assessment, he had been briefed on the deadly bomb attack, for which ISIS quickly claimed responsibility, in the northern city of Manbij'
word1 = 'brontosaurus'
num_of_entries = dict()

for letter in word:
  if letter in num_of_entries:
     num_of_entries[letter] +=1
  else:
     num_of_entries[letter] =1 
     
print ("Number of entries for word 'brontosaurus':")
for i, sum in num_of_entries.items():
    print(f"{i}= {sum}")
    