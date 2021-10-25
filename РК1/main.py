# Предметная область 9: 
# Операционная система - компьютер
# Запросы Д:
#   1.«Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список всех операционных систем, у которых название хранимой записи содержит "Windows", и названия компьютеров с этими ОС.
#   2.«Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список компьютеров со средней датой публикации операционных систем в каждом компьютере, отсортированный по средней дате публикации.
#     (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
#   3. «Операционная система» и «Компьютер» связаны соотношением многие-ко-многим.
#     Выведите список всех компьютеров, у которых название начинается с буквы «А», и список их операционных систем.

from operator import itemgetter
from store.computer import computers
from store.microprocessor import microprocessors
from store.microprocessor_computer import computers_with_microprocessor

def main():
  # Соединение данных один-ко-многим 
  microprocessor_join_computers = [{'microprocessor': o, 'computers': c}
    for o in microprocessors
    for c in computers 
    if o.computer_id == c.id
  ]

  print('Задание Д-1')
  # Выведем id, name, publication_year таблицы "microprocessor"
  # При этом name != Windows
  # И выведем компьютеры этих микропроцессоров
  D1 = [(x['microprocessor'].id, x['microprocessor'].name, x['microprocessor'].publication_year, x['computers'].name)
    for x in microprocessor_join_computers
    if x['microprocessor'].name.find('D9833') != - 1
  ]
  for x in D1:
    print(x)
  

  print('\nЗадание Д-2')
  # Выведем имя компьютера, среднее по дате публикации микропроцессоры этого компьютера
  # Сортируя по этому среднему

  # Заведем таблицу с накапливаемой суммой дат и кол-вом ОС:
  computer_sum_count_dict = {}
  for os_computers_row in microprocessor_join_computers:
    computer_name = os_computers_row['computers'].name
    publication_year = os_computers_row['microprocessor'].publication_year

    if computer_name in computer_sum_count_dict:
      computer_sum_count_dict[computer_name]['sum'] = computer_sum_count_dict[computer_name]['sum'] + publication_year
      computer_sum_count_dict[computer_name]['count'] = computer_sum_count_dict[computer_name]['count'] + 1
    else:
      computer_sum_count_dict[computer_name] = {'sum': publication_year, 'count': 1}

  D2 = sorted(
    [(computer_name, computer_sum_count_dict[computer_name]['sum'] / computer_sum_count_dict[computer_name]['count'])
      for computer_name in computer_sum_count_dict
      if computer_sum_count_dict[computer_name]['count'] != 0
    ],
    key=itemgetter(1), reverse=True
  )
  for x in D2:
    print(x)

  print('\nЗадание Д-3')

  # Соединение данных многие-ко-многим
  many_to_many = [(c.name, co.computer_id, co.microprocessor_id)
    for c in computers
        for co in computers_with_microprocessor
            if c.id == co.computer_id]



  computers_with_microprocessor_table = [(microprocessor.name, microprocessor.publication_year, computer_name)
    for computer_name, computer_id, microprocessor_id in many_to_many
        for microprocessor in microprocessors if microprocessor.id == microprocessor_id]

  D3 = {}
  for computer in computers:
    if computer.name.startswith('A'):
        microprocessor_of_computer = list(filter(lambda i: i[2] == computer.name, computers_with_microprocessor_table))
        microprocessor_names = [x for x, _, _ in microprocessor_of_computer]
        D3[computer.name] = microprocessor_names

  print(D3)
 
if __name__ == '__main__':
  main()
