import csv

def fRow(file):
    global firstRow
    global sortNames
    tmp = ''
    firstElem = 1
    for row in file:
        if firstElem == 0:
            # Заповнення першого ярдка для виведення 
            if tmp != row[1]:
                tmp = row[1]
                changeMonth(tmp)
                firstRow.append(tmp)
            # Розташування співробітників по алфавіту  
            
            if not(row[0] in sortNames):
                sortNames.append(row[0])   
        else:
            firstElem = 0        

    sortNames.sort()   

def changeMonth(date):
    month = date.split(sep = ' ', maxsplit = 1)
    print(month[0])

# Перший радок 
firstRow = []

# Список з відсортованими   
sortNames = []

# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)

# print(firstRow)
# print(sortNames)    