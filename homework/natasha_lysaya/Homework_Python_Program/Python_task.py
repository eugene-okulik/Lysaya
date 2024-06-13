import os
import sys
import argparse


def search_in_logs(file_path, search_text):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if search_text in line:
                    words = line.strip().split()
                    try:
                        index = words.index(search_text)
                        start = max(0, index - 5)
                        end = min(len(words), index + 6)
                        data = ' '.join(words[start:end])
                    except ValueError:
                        data = line.strip()

                    results.append((file_path, line_num, data))
    except Exception as e:
        print(f"Проблема со следующим файлом {file_path}: {e}")
    return results


def main():
    parser = argparse.ArgumentParser(description='Иинформация по поиску текста в логах.')
    parser.add_argument('-p', '--path', help='Путь к локальной папке с логами.')
    parser.add_argument('-t', '--text', help='Текст для поиска в логах.')
    parser.add_argument('-f', '--first', action='store_true', help='Отображать только первое совпадение.')

    args = parser.parse_args()

    logs_path = args.path

    if not os.path.isdir(logs_path):
        print(f"Данный путь к папке {logs_path} не валиден.")
        sys.exit(1)

    log_files = [os.path.join(logs_path, file) for file in os.listdir(logs_path) if
                 os.path.isfile(os.path.join(logs_path, file))]

    result_list = []
    for log_file in log_files:
        results = search_in_logs(log_file, args.text)
        if results:
            result_list.extend(results)
            if args.first:
                break

    if not result_list:
        print("Совпадений не найдено")
    else:
        for result in result_list:
            file_path, line_num, info = result
            print(f"Файл: {file_path}, Строка: {line_num}, Информация: {info}")


if __name__ == '__main__':
    main()


# python Python_task.py -p C:\Users\Lysaya_N\projects\Lysaya\homework\eugene_okulik\data\logs -t WARN
# python Python_task.py -p C:\Users\Lysaya_N\projects\Lysaya\homework\eugene_okulik\data\logs -t WARN -f
