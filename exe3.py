# -*- coding: utf-8 -*-
import requests                                            #θέλει εγκατάσταση του module requests
import json
import time
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()                  # Αυτές οι 2 εντολές χρησιμοποιούνται ώστε ο χρήστης να επιλέξει ένα αρχείο και από αυτό επιστρέφεται το 
filename = askopenfilename()     # path του.To αρχείο όμως που θα επιλεχθεί πρέπει να βρίσκεται στον ίδιο φάκελο με το εκτελέσιμο exe3.py γιατι αλλιώς εμφανίζεται error.Πιο συγκεκριμένα υπάρχει κάποιο πρόβλημα με τα path και τα αρχεία δεν γίνονται post αν βρίσκονται σε κάποιο άλλο φάκελο


params= {'apikey':'6e2757fe11a35a931cf09308b522bbeb9fc18ab81e377209add3b9b380b93721'}     #apikey που πηραμε με την εγγραφή στη σελίδα virustotal.com
files = {'file': (''+filename+'', open(''+filename+'', 'rb'))}  #το αρχείο που θέλουμε να στείλουμε για ανάλυση
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)  #στέλνουμε το αρχείο για scan
json_obj = response.json()                                                            #η απαντηση στο παραπάνω request
resource=json_obj.get('resource')                                                     #παίρνουμε τη τιμή του tag resource απ'το json
json_response =[]
starttime=time.time()                                                    
while True:
 params1 = {'apikey': '6e2757fe11a35a931cf09308b522bbeb9fc18ab81e377209add3b9b380b93721', 'resource': ''+resource+''}
                                                  #apikey, και χρησιμοποιούμε ως filter αναζητησης τη τιμή resource που πηραμε παραπάνω
 headers = {
  "Accept-Encoding": "gzip, deflate",             #χρειάζονται για να κάνουμε request , οπως αναφέρεται στο documentation της σελίδας
  "User-Agent" : "gzip,  stelios"
  }
 response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',      #η εντολη get που θέλουμε να γίνει
  params=params1, headers=headers)
  
 json_response = response.json()
 print json_response['verbose_msg']
 if json_response['response_code']==1:                                        #άν έχει γίνει το scan επιστρέφεται 1
   break
 time.sleep(20)        #αν δεν έχει γίνει η ανάλυση,το while επαναλαμβάνεται κάθε 20 δευτερόλεπτα.Αν ήταν 3 δευτερόλεπτα,που λέει η εκφώνηση της άσκησης, θα εμφανιζόταν error ,καθώς επειδή το apikey δεν ειναι premium , έχουμε τη δυνατότητα να κάνουμε το πολύ 4 requests κάθε λεπτό.

virusList =[]
json_response['scans'].keys()                                #εύρεση όλων τον κλειδιών στο json_response['scans']
for key in json_response['scans'].keys():                    #για κάθε κλειδι στο json_response['scans'] (τα κλειδια αναπαριστούν τα antivirus)
 if json_response['scans'][''+key+'']['detected'] == True :  #αν το tag detected είναι true,δηλαδη υπάρχει ιος
  virusList.append(''+key+'')                                #προστιθεται το αντιστοιχο antivirus στη λιστα
virusList.sort()                                             #Ταξινόμηση της λίστας
if len(virusList)==0:                                        #Αν η λίστα είναι κενή
 print 'No antivirus has marked the file as suspicious'      #Εμφανιζεται αντίστοιχο μηνυμα.Σημαίνει οτι κανένα antivirus δεν εντόπισε ιό
if len(virusList)>0:                                         #Αν η λιστα δεν ειναι κενή
  print virusList                                            #Εκτύπωση των antivirus που εντόπισαν ιό



