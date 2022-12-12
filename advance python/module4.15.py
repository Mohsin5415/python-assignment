
# When will the else part of try-except-else be executed? 

from os import fork 
 
if fork(): 
  print('foo') 
else: 
  print('bar') 