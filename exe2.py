# -*- coding: utf-8 -*-
trafficList = []
maxLengthList = 24                                      #������� ������� ������=4 ���� *6(���������/���)
while len(trafficList) < maxLengthList:     
 while True:
  try:
   item=int(input("Enter the number of the cars: "))           #�������� ��� ������� ��� ������� ��� ���� ���������
   trafficList.append(item)
  except :
   print("Input was wrong.Enter the number of the cars once more.")   # ��������� exception ��� ���� ��� ������� �������
   continue
  else:
   break
reportList = []
Max1= -1
Max2= -1
Max3= -1
Max4= -1
for i in range(24):                     
  if i < 6 :                                               #��� ��� 1� ���
   if trafficList[i] >Max1 : 
       Max1 = trafficList[i]                               #�� �������� > (������� ��� ���� ���) ������������ �� ��� �������
  elif i>=6 and i<12 :                                     #��� �� 2� ���
    if trafficList[i] >Max2:
	 Max2 = trafficList[i]
  elif i>=12 and i<18 :                                    #��� ��� 3� ���
    if trafficList[i] >Max3:
	 Max3 = trafficList[i]
  else:                                                    #��� ��� 4� ���
    if trafficList[i] >Max4:
	 Max4 = trafficList[i]
reportList = [('4:00pm', Max1), ('5:00pm', Max2), ('6:00pm', Max3), ('7:00pm', Max4)]   

print reportList                                            #�������� ��� �������� ��� ���� ��� ������