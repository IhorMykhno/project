import csv

def fRow(file):
    global firstRow
    tmp = ''
    for row in file:
        if tmp != row[1]:
            tmp = row[1]
            firstRow.append(tmp)

def sortN(file):
    global sortNames
    tmp = 1
    print(tmp)
    for names in file:
        if tmp == 0:
            t = names[0]
            sortNames.append(t)
        else:
            tmp = 0    

# Перший радок 
firstRow = []
# Список з відсортованими   
sortNames = []
# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    tmp = file_reader
    fRow(tmp)
    sortN(file_reader)
    
    
    # Зчитування даних з CSV файла
    # for row in file_reader:
        # print(f'{row[0]} {row[1]} {row[2]}')   
    # addTheDate(file_reader)    
print(firstRow)
print(sortNames)    