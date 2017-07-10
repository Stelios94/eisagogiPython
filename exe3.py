# -*- coding: utf-8 -*-
import requests                                            #����� ����������� ��� module requests
import json
import time
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()                  # ����� �� 2 ������� ���������������� ���� � ������� �� �������� ��� ������ ��� ��� ���� ������������ �� 
filename = askopenfilename()     # path ���.To ������ ���� ��� �� ��������� ������ �� ��������� ���� ���� ������ �� �� ���������� exe3.py ����� ������ ����������� error.��� ������������ ������� ������ �������� �� �� path ��� �� ������ ��� �������� post �� ���������� �� ������ ���� ������


params= {'apikey':'6e2757fe11a35a931cf09308b522bbeb9fc18ab81e377209add3b9b380b93721'}     #apikey ��� ������ �� ��� ������� ��� ������ virustotal.com
files = {'file': (''+filename+'', open(''+filename+'', 'rb'))}  #�� ������ ��� ������� �� ��������� ��� �������
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)  #��������� �� ������ ��� scan
json_obj = response.json()                                                            #� �������� ��� �������� request
resource=json_obj.get('resource')                                                     #��������� �� ���� ��� tag resource ��'�� json
json_response =[]
starttime=time.time()                                                    
while True:
 params1 = {'apikey': '6e2757fe11a35a931cf09308b522bbeb9fc18ab81e377209add3b9b380b93721', 'resource': ''+resource+''}
                                                  #apikey, ��� �������������� �� filter ���������� �� ���� resource ��� ������ ��������
 headers = {
  "Accept-Encoding": "gzip, deflate",             #����������� ��� �� ������� request , ���� ���������� ��� documentation ��� �������
  "User-Agent" : "gzip,  stelios"
  }
 response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',      #� ������ get ��� ������� �� �����
  params=params1, headers=headers)
  
 json_response = response.json()
 print json_response['verbose_msg']
 if json_response['response_code']==1:                                        #�� ���� ����� �� scan ������������ 1
   break
 time.sleep(20)        #�� ��� ���� ����� � �������,�� while ��������������� ���� 20 ������������.�� ���� 3 ������������,��� ���� � �������� ��� �������, �� ����������� error ,����� ������ �� apikey ��� ����� premium , ������ �� ���������� �� ������� �� ���� 4 requests ���� �����.

virusList =[]
json_response['scans'].keys()                                #������ ���� ��� �������� ��� json_response['scans']
for key in json_response['scans'].keys():                    #��� ���� ������ ��� json_response['scans'] (�� ������� ������������ �� antivirus)
 if json_response['scans'][''+key+'']['detected'] == True :  #�� �� tag detected ����� true,������ ������� ���
  virusList.append(''+key+'')                                #����������� �� ���������� antivirus ��� �����
virusList.sort()                                             #���������� ��� ������
if len(virusList)==0:                                        #�� � ����� ����� ����
 print 'No antivirus has marked the file as suspicious'      #����������� ���������� ������.�������� ��� ������ antivirus ��� �������� ��
if len(virusList)>0:                                         #�� � ����� ��� ����� ����
  print virusList                                            #�������� ��� antivirus ��� ��������� ��



