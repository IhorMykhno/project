import csv

# with open("C:/Interlink/acme_worksheet.csv", encoding='utf-8') as r_file:

# Читання даних з CSV документа
with open("C:/project/project/acme_worksheet.csv", encoding='utf-8') as r_file:    
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Зчитування даних з CSV файла
    for row in file_reader:
        print(f'{row[0]} {row[1]} {row[2]}')