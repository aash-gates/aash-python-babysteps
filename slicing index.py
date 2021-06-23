#A Demo Program on index Slice IBM Digital Nation

String = 'Alphabet'
slice = String[3:] #removing the 3 char from front 

slice = slice.upper()

print(slice)

import time
time.sleep(1.00)

# My Addition

rejoin = String[:3] #sparing the 3 char in front and removing the remaning char
print (rejoin)

import time
time.sleep(1.00)

slice = slice.lower() #fixint the case that was modified above with upper() function

print(rejoin + slice) #joing the resultant strings 

#end of the Program
