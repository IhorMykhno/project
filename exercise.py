import csv

def fRow(file):
    global firstRow
    tmp = ''
    for row in file:
        if tmp != row[1]:
            tmp = row[1]
            firstRow.append(tmp)

def sortN(Elements):
    global sortNames
    tmp = 1
    print(tmp)
    for names in Elements:
        if tmp == 0:
            if not(names[0] in sortNames):
                sortNames.append(names[0])   
        else:
            tmp = 0    
    sortNames.sort()   


# Перший радок 
firstRow = []
# Список з відсортованими   
sortNames = []
# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)
    sortN(file_reader)
    
    
    # Зчитування даних з CSV файла
    for row in file_reader:
        print(f'{row[0]} {row[1]} {row[2]}')   
    # addTheDate(file_reader)    
print(firstRow)
# print(sortNames)    