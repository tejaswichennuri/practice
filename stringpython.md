# practice
s=input()
t=int(input())
st=ord(s)
pt=chr(t)
print(st)
print(pt)
for i in range(65,97):
    print(chr(i),end="")
string="123" # returns true / "123ab" returns false
if string.isdigit():
    print("True")
else:
    print("False")
#string creation
s="hello"
st='hi'
str='''hello rey'''
print(s)
print(st)
print(str)
#string dlicing and indexing
s="python"
print(s[0])
print(s[:-1])
print( s[::2])
print(s[0:3])
print(s[:])
#looping through a string using for loop
str="python"
for char in s:
    print(char)
#count all uppercase letters
s="Hello World"
count=0
for ch in s:
    if(ch.isupper()):
        count+=1
print(count)
#count vowels in a string
def count_vowels(s):
    vowel="aeiou"
    count=0
    for ch in s.lower():
        if ch in vowel:
            count+=1
    return count
print(count_vowels("Hello World")) 
#check string is palindrome or not
def is_palindrome(s):
    s=s.lower()
    x=s[::-1]
    return s==x
print(is_palindrome("madam"))
#remove all digits from a string
def remove_str(s):
    result=""
    for ch in s:
        if not ch.isdigit():
            result+=ch
    return result
print(remove_str("abc567dcfr45")) 
#find frequency
def frequency_is(s):
   for ch in set(s):
       print(f"{ch}:{s.count(ch)}")
frequency_is("banana")
#using title tag
s="python is famous language"
print(s.title())
#isalpha
s="HelloWorld123"
x="Hwlloteju"
print(s.isalpha())
print(x.isalpha())
#replace 
s="python is powerful"
print(s.replace(" ","-"))
#split
s="python is fn and easy"
word=s.split()
print(len(word))
#isalnum
s="abc123"
print(s.isalnum())
#reverse a string 
def reverse_str(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
print(reverse_str("hello"))
#anagram
def is_anagram(s1,s2):
    return sorted(s1)==sorted(s2)
print(is_anagram("listen","silent"))
#remove duplicate char from str
def remove_dup(s):
    result=""
    for ch in s:
        if ch not in result:
            result+=ch
    return result
print(remove_dup("programming"))
#isdigit
s="1234"
print(s.isdigit())
#count no of words in a sentence
s="programming skills are more imp"
print(len(s.split()))


    
    

