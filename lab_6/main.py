import csv
from time import sleep
from random import randint

FILE_IN = "C:\BD\CSVs\plants_employees.csv"
srez = 10


def main():
    file_numb = 0
    while True:
        file_numb += 1
        file_out =  f"C:\BD\Docker\\nifi\in_file\\file_{file_numb}.csv"
        f_out = open(file_out, 'w', newline='', encoding='utf-8')
        writer = csv.writer(f_out)
        writer.writerow(["PlantD", "EmployeeID"])

        for i in range(5):
            writer.writerow([randint(1, 1191), randint(1, 70)])

        f_out.close()

        sleep(10)


if __name__ == '__main__':
    main()
