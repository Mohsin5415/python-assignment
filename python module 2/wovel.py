# Write a Python program to test whether a passed letter is a vowel or not

ch = input("enter the alphabet : ")

if ch in ('a','e','i','o','u','A','E','I','O','U'):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")