#1. Дан список строк my_list. Создать новый список в который поместить
#элементы из my_list по следующему правилу:
#Если строка стоит на нечетном месте в my_list, то ее заменить на
#перевернутую строку. "qwe" на "ewq".
#Если на четном - оставить без изменения.
#Задание сделать с использованием enumerate или range.


# В случае если мы считаем  0, 1, 2 ( 0 не трогаем, 1 нечетная, 2 четная)
my_list = ["qwe", "row", "typ", "pol"]
my_new_list = []
for index, frame in enumerate(my_list):
    if index % 2:
        my_new_list.append(frame[::-1])
    else:
        my_new_list.append(frame)
print(my_new_list)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a"
my_list = ["qwe", "arow", "typ", "apol"]
my_new_list = []
for element in my_list:
    if element[0] == 'a':
        my_new_list.append(element)
print(my_new_list)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ["qwae", "arow", "typ", "apol"]
my_new_list = []
for element in my_list:
    if "a"in element:
        my_new_list.append(element)
print(my_new_list)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.

persons = [{"name": "John", "age": 15},
           {"name": "Anna", "age": 23},
           {"name": "Dan", "age": 5},
           {"name": "Maximusss", "age": 24},
           {"name": "Olgha", "age": 25},
           {"name": "Volodymyr", "age": 5},
           {"name": "Jack", "age": 45}]

ages = []
names_lens = []
youngest_persons = []
long_name_persons = []

for person_dict in persons:
    ages.append(person_dict["age"])
    names_lens.append(len(person_dict["name"]))

min_age = min(ages)
max_len_name = max(names_lens)


for person_dict in persons:
    if person_dict["age"] == min_age:
        youngest_persons.append(person_dict["name"])
    if len(person_dict["name"]) == max_len_name:
        long_name_persons.append(person_dict["name"])

mean_age = sum(ages) / len(ages)

print(youngest_persons, long_name_persons, mean_age)

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
my_dict_2 = {11: 11, 2: 22}

result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print(result_1)

result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
print(result_2)

result_3 = {key: my_dict_1[key] for key in result_2}
print(result_3)

result_4 = my_dict_1.copy()
for key in my_dict_2:
    if key in result_4:
        result_4[key] = [result_4[key], my_dict_2[key]]
    else:
        result_4[key] = my_dict_2[key]
print(result_4)
