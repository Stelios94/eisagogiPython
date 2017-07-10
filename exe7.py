# -*- coding: utf-8 -*-
item=raw_input("Enter a text : ")                             #Εισαγωγή κειμένου απ'τον χρήστη
while item.strip() == "":
    item= raw_input("Invalid Input.Enter a text : ")          #Αν δωσει κενό input ,πρέπει να δωσει νέο text
words=item.split()                                            #διαχωρισμός του input σε λεξεις οταν εμφανίζεται κενό
maxLength=-1
for element in words:                                         #για κάθε στοιχείο της λίστας words εκτελείται η επανάληψη
 if len(element)>= maxLength:                                 #αν το μήκος του ελεγχόμενου στoιχείου ειναι μεγαλυτερο Ή ΙΣΟ του maxLength
  maxLength=len(element)                                      #ανανεώνεται το maxLength
  printedWord=element                                         #το στοιχείο αντικαθιστά την παλιά λέξη προς εκτύπωση
print printedWord                                             #εκτύπωση της printedWord ,δηλαδή της λέξης με το μεγαλύτερο μήκος