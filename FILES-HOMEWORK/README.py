# Задание №1

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        number_ingredients = int(file.readline())
        lst = []
        for _ in range(number_ingredients):
            name_ingredient, quantity, measure = file.readline().strip().split(' | ')
            lst.append({'ingredient_name': name_ingredient,
                        'quantity': quantity,
                        'measure': measure})
        file.readline()
        cook_book[dish_name] = lst

from pprint import pprint
pprint(cook_book, indent=6)
print()


# Задание №2
def all_dishes():
    lst = []
    for _ in cook_book:
        lst.append(_)
    return lst


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for _ in dishes:
        for i in cook_book[_]:
            name_ing, measure, quantity = i['ingredient_name'], i['measure'], i['quantity']
            if name_ing in all_ingredients:
                all_ingredients[name_ing]['quantity'] += quantity
            else:
                all_ingredients[name_ing] = {'measure': measure, 'quantity': quantity}
    for _ in all_ingredients:
        all_ingredients[_]['quantity'] = int(all_ingredients[_]['quantity']) * person_count
    return all_ingredients


pprint(get_shop_list_by_dishes(all_dishes(), 8))

# Задание №3
with open('1.txt', 'r', encoding='utf-8') as file1, open('2.txt', 'r', encoding='utf-8') as file2, \
        open('3.txt', 'r', encoding='utf-8') as file3, open('finish_file.txt', 'w', encoding='utf-8') as file4:
    lst1 = file1.readlines()
    lst2 = file2.readlines()
    lst3 = file3.readlines()
    all_lst = {len(lst1): {'name': '1.txt', 'lst': lst1}, len(lst2): {'name': '2.txt', 'lst': lst2},
               len(lst3): {'name': '3.txt', 'lst': lst3}}
    for _ in range(min(all_lst), max(all_lst)+1):
        if _ in all_lst:
            file4.write(f'{all_lst[_]["name"]}\n{_}\n{"".join(all_lst[_]["lst"])}\n')
