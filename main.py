from pprint import pprint


def get_info(file_name, mode, encoding):
    data = {}
    with open(file_name, mode, encoding=encoding) as file:
        for line in file:
            dish = line.strip()
            counter = int(file.readline())
            temp_list = []
            for item in range(counter):
                name, quantity, measure = file.readline().split("|")
                temp_list.append(
                    {"ingredient_name": name.strip(), "quantity": quantity.strip(), "measure": measure.strip()}
                )
            data[dish] = temp_list
            file.readline()
    return data


cook_book = get_info('Recipes.txt', 'r', 'utf-8')


# pprint(cook_book)


# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон
# для кого мы будем готовить

def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for meal in dishes:
        if meal in cook_book:
            for ingredient in cook_book[meal]:
                if ingredient['ingredient_name'] not in shop_list:
                    in_qu = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
                    shop_list[ingredient['ingredient_name']] = in_qu
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list


# pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 2))
