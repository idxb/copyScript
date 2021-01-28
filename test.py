import os, datetime, fnmatch, shutil

# текущий год  -year
now = datetime.datetime.now()
year = str(now.year)

# месяц за текущим - month
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь']
month = str(now.month)
month = months[(int(month) - 1) + 1]

base_path = '//uk-auto-exp10.2gis.local/ExportResults/'
projects = ['Tyumen', 'Tobolsk', 'Ryazan', 'Ivanovo']
cites_ru = ['Тюмень', 'Тобольск', 'Рязань', 'Иваново', 'Хужгород']


# поиск последнего проекта в папке base_path
def find_project_path(project, bases_path):
    # получаем список всех папок по пути base_path
    exp_results = os.listdir(path=bases_path)
    # ищем в списке exp_results по regexp совпадения и заносим в список filtered_results
    filtered_results = fnmatch.filter(exp_results, 'DGDAT.Desktop-' + project + '*')
    # сортируем полученный список по времени в обратном порядке и вычленяем первый элемент в result_item
    result_item = (sorted(filtered_results, reverse=True)).pop(0)
    result_item = bases_path + result_item
    return result_item


last_project_path = find_project_path(projects[0], base_path)
print(last_project_path)


def find_source_path(city, current_year, current_month):
    base_folders_path = '//ewuk-adc02/CityShares/' + city + '/!Сборочки/' + current_year + '/' + current_month
    # Проверяем существует ли папака
    if os.path.exists(base_folders_path):
        pass

    else:
        print('Creating folder')
        os.mkdir(base_folders_path)
        return


def copy_files(source, distonation, ):
    source = base_path + result_item + '/' + filename
    distanation = '//ewuk-adc02/CityShares/' + city + '/!Сборочки/' + year + '/' + month
    if os.path.exists():
        print(base_path + '/' + result_item)
        shutil.copy('')

        print('Копируем...')
    else:
        print('Что-то пошло не так')


# copy_files('Tyumen.dgdat', r'\\ewuk-adc02\CityShares\Тобольск\!Сборочки\2021\Февраль', result_item, base_path)


# print('Какой регион был выгружен?')
# print(' 1 - Тюмень\n', '2 - Тобольск\n', '3 - Иваново\n', '4 - Рязань\n')
user_input = input()

file_name = projects[int(user_input)] + '.dgdat'

print(file_name)

paste_folders_check(cites_ru[1], year, month)

# TODO выбор папки в сборочках (создать, если нет такой)
# TODO копирование из папки в сети на сервере в папку в сборочках
# TODO отслеживание готовности копирования по прогресс бару
# TODO по готовности разархивировать файл в ту же папку
# TODO отслеживание по прогресс бару
# TODO копировать ссылку на файл в буфер и издать звуковой сигнал
