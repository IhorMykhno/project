import csv
import os
from inspect import getsourcefile
from os.path import abspath, dirname

def fRow(file):
    global firstRow
    global sortNames
    global allStuff

    # Допоміжна зміння для формування першого рядка в CSV
    tmp = ''
    # Індекс списку
    iList = 0
    # Відкидання першого елемента
    firstElem = 1

    for row in file:
        if firstElem == 0:
            # Заповнення першого ярдка для виведення 
            if tmp != row[1]:
                tmp = row[1]
                # changeMonth(tmp)
                firstRow.append(tmp)

            # Розташування співробітників по алфавіту  
            if not(row[0] in sortNames):
                sortNames.append(row[0])   

            # Створення списку з 3 елементів
            allStuff.append([])
            allStuff[iList].append(row[0])
            allStuff[iList].append(row[1])
            allStuff[iList].append(row[2])
            iList += 1

        else:
            firstElem = 0        
    sortNames.sort()   

def changeMonth(date):
    # Зберігаються відредаговані дані першого рядка
    newDate = []
    newDate.append('Name/Date')

    for i in range(len(date)):
        month = date[i]
        # Розбиття вхідної дати 
        month = month.split(sep = ' ', maxsplit = 2)
        # Генерування дати поданої в шаблоні
        newMonth = f'{month[2]}-{searchMonth(month[0])}-{month[1]}'
        newDate.append(newMonth)
    return newDate   

def searchMonth(month):
    allMonth = {
        'Jan' : '01',
        'Feb' : '02', 
        'Mar' : '03',
        'Apr' : '04',
        'May' : '05',
        'Jun' : '06',
        'Jul' : '07',
        'Aug' : '08', 
        'Sept' : '09',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
    }
    return allMonth[month]

def newStuffList():
    global firstRow
    global sortNames
    global allStuff
    global NewCSVdoc
    # Лічильник сформованого списку
    counter = 0
    for sName in sortNames:
        NewCSVdoc.append([])
        NewCSVdoc[counter].append(sName)
        # Заповнення в новому списку 0 рядка робочих часів
        for j in range(1, len(firstRow)+1):
            NewCSVdoc[counter].append(0)

        for i in range(len(allStuff)):
            # Підстановка відповідного ім'я по алфавіту
            if sName == allStuff[i][0]:
                idx =  firstRow.index(allStuff[i][1]) 
                NewCSVdoc[counter][idx+1] = allStuff[i][2]  
        counter += 1            

def srchCatalog():
    path = abspath(getsourcefile(lambda:0))
    path = dirname(path)  
    path = path + "\\acme_worksheet.csv"
    return path

# Перший радок для CSV документу
firstRow = []

# Список з відсортованими іменами  
sortNames = []

# Всі дані про співробітників
allStuff = []

# Список з даними, які будуть виводитись в новий CSV
NewCSVdoc = []

#Пошук шляху до CSV файла 
linkOfCatalog = srchCatalog()

# Читання даних з CSV документа
with open(linkOfCatalog, encoding='utf-8') as r_file:   
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)

# Формування даних для виведення в новий CSV
newStuffList()

# Редагування першого рядка за шаблоном
firstRow = changeMonth(firstRow)

# Виведення 
with open("C:/project/project/new_acme_worksheet.csv", 'w', newline="") as w_file:    
     writer = csv.writer(w_file)
     writer.writerows([firstRow])
     writer.writerows(NewCSVdoc)