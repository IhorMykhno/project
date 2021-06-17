import csv

def fRow(file):
    global firstRow
    tmp = ''
    for row in file_reader:
        if tmp != row[1]:
            tmp = row[1]
            firstRow.append(tmp)

# Перший радок 
firstRow = []
# Словник з датами 
# dictDate = {}
# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    fRow(file_reader)

    # Зчитування даних з CSV файла
    # for row in file_reader:
        # print(f'{row[0]} {row[1]} {row[2]}')   
    # addTheDate(file_reader)    
print(firstRow)    