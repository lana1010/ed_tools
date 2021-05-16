"""
***************************************************************************************
*Your data.json should look like this:
*
*{
* "maps":[
*         {"id":"blabla","iscategorical":"0"},
*         {"id":"blabla","iscategorical":"0"}
*        ],
*"masks":
*         {"id":"valore"},
*"om_points":"value",
*"parameters":
*         {"id":"valore"}
*}
*Your code should be:
*
*import json
*from pprint import pprint
*
*with open('data.json') as data_file:    
*    data = json.load(data_file)
*pprint(data)
*
***************************************************************************************
*Note that this only works in Python 2.6 and up, as it depends upon the with-statement.
***************************************************************************************
"""

import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
pprint(data)

pprint (data["maps"][0]["id"])  # will return 'blabla'
print data["masks"]["id"]    # will return 'valore'
print data["om_points"]      # will return 'value'