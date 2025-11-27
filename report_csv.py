import argparse
import csv
from tabulate import tabulate




def read_files(files):
    """Чтение data из файлов CSV"""
    data = []
    for file_patch in files:
        # добавление пути files/ если не указан полный путь
        if not file_patch.startswith(('/','./','../')):
            file_patch = f"files/{file_patch}"

            try:
                with open(file_patch, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        data.append(row)
            except FileNotFoundError:
                print('Ошибка чтения файлов: не найден')
            except Exception as err:
                print('Ошибка при чтении файлов: что-то пошло не так')

    return data



def generate_performance_report(data):
    """Генерация отчета по performance"""
    #статистика
    statistic = {}

    for worker in data:
        position = worker['position']
        performance = float(worker['performance'])

        if position not in statistic:
            statistic[position] = {'total':0, 'count':0}

        statistic[position]['total'] += performance
        statistic[position]['count'] += 1

    #Расчет avg performance
    report_data = []
    for position, stats in statistic.items():
        avg_performance = stats['total']/stats['count']
        report_data.append([position, round(avg_performance, 2)])

    #сортировка
    report_data.sort(key=lambda x:x[1], reverse=True)

    return report_data

def main():
    parser = argparse.ArgumentParser(description='Тестовое задание')
    parser.add_argument('--files', nargs='+', required=True, help='Путь к файлам(СSV)')
    parser.add_argument('--report', required=True, choices=['performance'], help='Тип отчета')
    args = parser.parse_args()

    data = read_files(args.files) #вызываем чтение

    #проверка ключа отчета
    if args.report == 'performance':
        report_data = generate_performance_report(data)

        #составление таблицы
        number_data = [[i+1] + row for i, row in enumerate(report_data)]
        headers = ['', 'position', 'performance']
        print(tabulate(number_data,headers=headers, tablefmt='simple'))

if __name__ == '__main__':
    main()