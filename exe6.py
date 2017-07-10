# -*- coding: utf-8 -*-
import urllib2
import json
url= "https://api.chucknorris.io/jokes/random"   
hdr = {'User-Agent': 'Mozilla/5.0'}              #����� header mozilla ��� �� ��������� � ����� ��� api
req = urllib2.Request(url,headers=hdr)         
json_obj = urllib2.urlopen(req)                 
data= json.load(json_obj)                        #�� ������������ ��� api ����� �� ����� json
print data['value']
string= data['value']                            #���������� ��� tag value �� string
words=string.split()                             #��������� �� string �� ������ ���� ��������� ����
finalList =[]  
for element in words:                            #��� ���� �������� ��� ����� words ���������� � ���������
 if len(element)>2:                              #�� �� ����� ��� ��������� ����� ���������� ��� 2
  firstLetter=element[0]                         #������ ����������
  lastLetter=element[-1]                         #���������� ����������
  firstNumber=ord(firstLetter)                   #��������� ��� 1�� ��������� �� ������
  lastNumber=ord(lastLetter)                     #��������� ��� 2�� ��������� �� ������
  final=(firstNumber + lastNumber) % 3           #�������� ��� 2 ��� �������� �� �� 3
  finalList.append(final)                        #�������� ��� ��������� �������� ��� ������ finalList
 else:                                           #������,�� �� ����� ����� <=2
  finalList.append(-1)
print finalList                                  #�������� ��� ������� ������
