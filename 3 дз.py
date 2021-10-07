from pprint import pprint


def length_of(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = len(file.readlines())
        return data


def make_dict(files_list):
    temp = {}
    for file_name in files_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            str_counter = length_of(file_name)
            data = file.read()
            x = {file_name: (str_counter, data)}
            temp.update(x)
    return temp


def sorted_dict(file_name):
    for files in sorted(unsorted_dict.items(), key=lambda i: i[1]):
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(f'{files[0]}\n')
            for a in files[1]:
                f.write(f'{a}\n')


file_list = ['1.txt', '2.txt', '3.txt']
unsorted_dict = make_dict(file_list)
# print(unsorted_dict)
sorted_dict(unsorted_dict)
