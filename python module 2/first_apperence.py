"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""
str='The Lyrics Is Not That Poor'
pos_not =str.find("Not")
pos_poor = str.find("Poor")

if pos_not < pos_poor:
 print(str[:pos_not]+"good")
