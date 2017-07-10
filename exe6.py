# -*- coding: utf-8 -*-
import urllib2
import json
url= "https://api.chucknorris.io/jokes/random"   
hdr = {'User-Agent': 'Mozilla/5.0'}              #χρήση header mozilla για να επιτραπεί η χρήση του api
req = urllib2.Request(url,headers=hdr)         
json_obj = urllib2.urlopen(req)                 
data= json.load(json_obj)                        #τα αποτελέσματα του api είναι σε μορφη json
print data['value']
string= data['value']                            #αποθήκευση του tag value σε string
words=string.split()                             #χωρίζουμε το string σε λέξεις οταν συνανταμε κενό
finalList =[]  
for element in words:                            #για κάθε στοιχείο στη λιστα words εκτελείται η επανάληψη
 if len(element)>2:                              #αν το μήκος του στοιχείου ειναι μεγαλύτερο του 2
  firstLetter=element[0]                         #πρώτος χαρακτήρας
  lastLetter=element[-1]                         #τελευταιος χαρακτήρας
  firstNumber=ord(firstLetter)                   #μετατροπή του 1ου χαρακτήρα σε αριθμό
  lastNumber=ord(lastLetter)                     #μετατροπή του 2ου χαρακτήρα σε αριθμό
  final=(firstNumber + lastNumber) % 3           #άθροισμα των 2 και υπόποιπο με το 3
  finalList.append(final)                        #πρόσθεση σαν τελευταίο στοιχείο της λιστας finalList
 else:                                           #αλλιώς,αν το μήκος ειναι <=2
  finalList.append(-1)
print finalList                                  #εκτύπωση της τελικής λίστας
