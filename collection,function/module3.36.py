# How Do You Check The Presence Of A Key In A Dictionary? 

def checkKey(dic, key):
     
    if dic.has_key(key):
        print("Present, value =", dic[key])
    else:
        print("Not present")
 
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
 
key = 'w'
checkKey(dic, key)