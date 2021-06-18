import csv

def fRow(file):
    global firstRow
    global sortNames
    global allStuff
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
    newDate = []
    newDate.append('Name/Date')
    # print(date)
    for i in range(len(date)):
        month = date[i]
        # Розбиття вхідної дати 
        month = month.split(sep = ' ', maxsplit = 2)
        # Генерування дати поданої в шаблоні
        newMonth = f'{month[2]}-{searchMonth(month[0])}-{month[1]}'
        # newMonth = month[2] + searchMonth(month[0]) + month[1]
        newDate.append(newMonth)
    # print(newDate)
    return newDate   
    # date[0] = searchMonth(month)
    # Заміна на числове позначення місяця
    # date = date.replace(month, searchMonth(month))

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
    tmp = 0
    for sName in sortNames:
        NewCSVdoc.append([])
        NewCSVdoc[tmp].append(sName)
        # Заповнення в новому списку 0 рядка робочих часів
        for j in range(1, len(firstRow)+1):
            NewCSVdoc[tmp].append(0)

        for i in range(len(allStuff)):
            # Підстановка відповідного ім'я по алфавіту
            if sName == allStuff[i][0]:
                idx =  firstRow.index(allStuff[i][1]) 
                # print(idx)
                # print(allStuff[i][2])
                NewCSVdoc[tmp][idx+1] = allStuff[i][2]  
                # NewCSVdoc[tmp].append(allStuff[i][1])
        tmp += 1            

# Перший радок 
firstRow = []

# Список з відсортованими   
sortNames = []

# Перелік даних про співробітників
allStuff = []

# Список з даними які будуть виводитись в новий CSV
NewCSVdoc = []

# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)

newStuffList()
firstRow = changeMonth(firstRow)

print(firstRow)
print(NewCSVdoc)

# Виведення 
with open("C:/project/project/new_acme_worksheet.csv", 'w', newline="") as w_file:    
     writer = csv.writer(w_file)
     writer.writerows([firstRow])
     writer.writerows(NewCSVdoc)