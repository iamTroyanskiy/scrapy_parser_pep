import csv


def dict_to_csv(file_path, dict_data, head):
    file = [head]
    file.extend(dict_data.items())
    file.append(('Total', sum(dict_data.values())))
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(file)
    except IOError as error:
        print(str(error))
