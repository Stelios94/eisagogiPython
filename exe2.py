# -*- coding: utf-8 -*-
trafficList = []
maxLengthList = 24                                      #μεγιστο μεγεθος λιστας=4 ωρες *6(δεκαλεπτα/ωρα)
while len(trafficList) < maxLengthList:     
 while True:
  try:
   item=int(input("Enter the number of the cars: "))           #εισαγωγη των αμαξιων που περασαν για καθε δεκαλεπτο
   trafficList.append(item)
  except :
   print("Input was wrong.Enter the number of the cars once more.")   # χειρισμός exception για όταν δεν δίνεται αριθμος
   continue
  else:
   break
reportList = []
Max1= -1
Max2= -1
Max3= -1
Max4= -1
for i in range(24):                     
  if i < 6 :                                               #για την 1η ωρα
   if trafficList[i] >Max1 : 
       Max1 = trafficList[i]                               #Αν στοιχείο > (μεγιστο της ωρας του) αποθηκεύεται ως νεο μεγιστο
  elif i>=6 and i<12 :                                     #για τη 2η ωρα
    if trafficList[i] >Max2:
	 Max2 = trafficList[i]
  elif i>=12 and i<18 :                                    #για την 3η ωρα
    if trafficList[i] >Max3:
	 Max3 = trafficList[i]
  else:                                                    #για την 4η ωρα
    if trafficList[i] >Max4:
	 Max4 = trafficList[i]
reportList = [('4:00pm', Max1), ('5:00pm', Max2), ('6:00pm', Max3), ('7:00pm', Max4)]   

print reportList                                            #εκτυπωση των μεγιστων για καθε ωρα αιχμης
