###########################################
#
# stringAligning
# 
#
###########################################


# 1) deafault formatting
s='The sword of truth'
aa="{0}".format(s)
print ("{0}".format(s))
print("1. "+"*"+aa+"*")
#>>>The sword of truth

# 2) minimum width 25
aa="{0:25}".format(s)
print("2. ""*"+aa+"*")
#>>*The sword of truth       *

# 3) right align, min width 25
aa="{0:>25}".format(s)
print("3. "+"*"+aa+"*")
#>>*       The sword of truth*

# 4) center align, min width 25
aa="{0:^25}".format(s)
print("4. ""*"+aa+"*")
#>>*   The sword of truth    *

# 5) - fill, center align, min width 25
aa="{0:-^25}".format(s)
print("5. ""*"+aa+"*")
#>>*---The sword of truth----*

# 6) . fill, left align, min width 25
aa="{0:.<25}".format(s)
print("6. ""*"+aa+"*")
#>>*The sword of truth.......*

# 7) max width 10
aa="{0:.10}".format(s)
print("7. ""*"+aa+"*")
#>>*The sword *
