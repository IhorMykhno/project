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
    # Початковий місяць
    month = (date.split(sep = ' ', maxsplit = 1))[0]
    # Заміна на числове позначення місяця
    date = date.replace(month, searchMonth(month))

def searchMonth(month):
    allMonth = {
        'Jan' : '1',
        'Feb' : '2', 
        'Mar' : '3',
        'Apr' : '4',
        'May' : '5',
        'Jun' : '6',
        'Jul' : '7',
        'Aug' : '8', 
        'Sept' : '9',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
    }
    return allMonth[month]


# Перший радок 
firstRow = []

# Список з відсортованими   
sortNames = []

# 
allStuff = []

# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)

# print(firstRow)
# print(sortNames)  
allStuff.sort(key = lambda x: x[0][0])
print(allStuff)
