# -*- coding: utf-8 -*-
item=raw_input("Enter a text : ")                             #�������� �������� ��'��� ������
while item.strip() == "":
    item= raw_input("Invalid Input.Enter a text : ")          #�� ����� ���� input ,������ �� ����� ��� text
words=item.split()                                            #����������� ��� input �� ������ ���� ����������� ����
maxLength=-1
for element in words:                                         #��� ���� �������� ��� ������ words ���������� � ���������
 if len(element)>= maxLength:                                 #�� �� ����� ��� ����������� ��o������ ����� ���������� � ��� ��� maxLength
  maxLength=len(element)                                      #����������� �� maxLength
  printedWord=element                                         #�� �������� ����������� ��� ����� ���� ���� ��������
print printedWord                                             #�������� ��� printedWord ,������ ��� ����� �� �� ���������� �����