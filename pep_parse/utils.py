import csv


def dict_to_csv(file_path, dict_data, head):
    file = [head]
    file.extend(dict_data.items())
    file.append(('Total', sum(dict_data.values())))
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(file)
