import csv
from typing import Literal

titulos_das_paginas = []

# Read CSV
move_to_back_i = 0
qa_list = None
with open("./qa.csv", "rt") as qa_csv:
    qa_list = list(csv.reader(qa_csv, dialect="excel"))
    #print("csv carregado")


def radix_sort_lsd(original_list, column_index, asc=True):
    max_fill = max([len(original_record[column_index]) for original_record in original_list])
    for original_list_i in original_list:
        original_list_i[column_index] = original_list_i[column_index].ljust(max_fill, '\0')
    ordered_list_by_str = original_list
    for char_i in range(max_fill)[::-1]:
        ordered_list_by_str = counting_sort(ordered_list_by_str, column_index,asc=asc, data_type="str",string_i=char_i)
    for ordered_record in ordered_list_by_str:
        ordered_record[column_index] = ordered_record[column_index].strip("\0")
    return ordered_list_by_str

# Counting Sort with int
def counting_sort(original_list, column_index: int, asc=True, data_type: Literal["int", "str"]="int", string_i=0):
    if data_type == "int":
        unordered_column = [int(original_record[column_index]) for original_record in original_list]
    elif data_type == "str":
        unordered_column = [ord(original_record[column_index][string_i]) for original_record in original_list]
    start_offset = min(unordered_column)
    histogram_length = (max(unordered_column) - start_offset) + 1
    histogram = [0] * histogram_length

    def get_index_from(value):
        if (value >= start_offset) and (value < (start_offset + histogram_length)):
            return value - start_offset
        else:
            raise IndexError
    
    for unordered_element in unordered_column:
        histogram[get_index_from(unordered_element)] += 1
    last_index_list = histogram
    last_index = -1
    for hi in range(len(histogram))[::(-1 + asc*2)]:
        last_index += last_index_list[hi]
        last_index_list[hi] = last_index

    ordered_list = [0] * len(original_list)

    for original_list_index in range(len(original_list))[::-1]:
        ordered_list[last_index_list[get_index_from(unordered_column[original_list_index])]] = original_list[original_list_index]
        last_index_list[get_index_from(unordered_column[original_list_index])] -= 1
    
    return ordered_list

#print(counting_sort(qa_list[1:], 0))

qa_csv_header = qa_list[0]
qa_list = counting_sort(qa_list[1:], 3, asc=False)
qa_list = radix_sort_lsd(qa_list,0)
qa_list.insert(0, qa_csv_header)
print(qa_list)

# Building index table 
qa_categories = set()
qa_categories.add(qa_list[1][0])
qa_index_table = [[qa_list[1][0], 1]]

for qa_i in range(2, len(qa_list)):
    set_size = len(qa_categories)
    qa_categories.add(qa_list[qa_i][0])
    set_size -= len(qa_categories)
    if (set_size == -1):
        qa_index_table.append([qa_list[qa_i][0], qa_i])

#print(qa_index_table)

# Sequencial Search with Sentry/Sentinel with "move-to-front" reverse method in Index Table
def qa_index_table_sequencial_search(category):
    global move_to_back_i
    # Sentry
    qa_index_table.append([category, -1])
    
    counter = 0
    while(True):
        if qa_index_table[counter][0] == category:
            break
        counter += 1

    if counter == len(qa_index_table)-1:
        return qa_index_table.pop()
    else:
        # "move-to-back" as no category should be searched 2 times.
        qa_index_table.pop()
        result = qa_index_table[counter].copy()
        qa_index_table[counter] = qa_index_table[move_to_back_i-1].copy()
        qa_index_table[move_to_back_i-1] = result
        move_to_back_i = -1* ((abs(move_to_back_i) + 1) % len(qa_index_table))
        return result

    # Old sequencial search
    #
    # for qa_index_table_item in qa_index_table:
    #     if qa_index_table_item[0] == category:
    #         return qa_index_table_item
    # return [category, -1]

# Filter questions by using Index Table.
def qa_filter(category):
    result = []
    start_i = qa_index_table_sequencial_search(category)[1]
    if start_i == -1:
        return result
    for i in range(start_i, len(qa_list)):
        if qa_list[i][0] != category:
            break
        result.append(qa_list[i])
    return result

#print(qa_filter("Oauth2"))
#print(qa_index_table)
#print(qa_filter("Aprendizado de Máquina"))
#print(qa_index_table)
#print(qa_filter("Arquitetura de Inteligência de Negócio"))
#print(qa_index_table)
#print(qa_filter("Outro"))
#print(qa_index_table)

def qa_format(qa_selected):
    # Format Questions and Answers Here
    return "<br>".join([", ".join(i) for i in qa_selected])

def on_post_page_macros(env):
    if env.page.title == "Simulado":
        ...
    else:
        titulos_das_paginas.append(env.page.title)
        qa_filtered = qa_filter(env.page.title)
        env.markdown += qa_format(qa_filtered)


def define_env(env):
    #env.variables["titulos_das_paginas"] = titulos_das_paginas

    @env.macro
    def create_mock_test_menu():
        titulos_das_paginas_html = "<form>"
        for titulo in titulos_das_paginas:
            titulos_das_paginas_html += f'<input type="radio" id="{titulo}" name="priorized_category" value="{titulo}">\n<label for="{titulo}">{titulo}</label><br>'
        titulos_das_paginas_html += "</form>"
        print(titulos_das_paginas_html)
        return titulos_das_paginas_html
    

# Scrapped Idea
# def define_env(env):
#     @env.macro
#     def load_qa(category):
#         #qa_filtered = qa_filter(qa_list, category)
#         #print(qa_filtered)
#         #print([i for i in qa_list])
#         ...