import zipfile, os, shutil, datetime, winsound
from time import sleep
from tqdm import trange

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

# # d:\dp\copyScript получение рабочей деректории
# dir = os.getcwd()
#
# # выведем путь
# print(dir)
# # dir = '//tmn-srv01/public'
#
# # проверка существования папки
# print(os.path.exists(dir))
#
# # является ли папка каталогом
# print(os.path.isdir(dir))
#
# # получить базовый путь
# print(os.path.dirname(dir))
#
# # получить имя папки
# print(os.path.basename(dir))
#
# # является ли путь файлом
# print(os.path.isfile(dir))
#
# # добавить в путь
# new_dir = os.path.join(dir, 'foo')
# print(new_dir)
#
# zip_place = 'C:/1/'

# if os.path.exists(zip_place):
#     print("Exist")
# else:
#     print('Directory not found!')
now = datetime.datetime.now()

# путь до выгрузок
bases_path = '//uk-auto-exp10.2gis.local/2GISExportService/ExportResults'
# имя файла
file = 'tyumen_DgdatDesktop_2020-12-29T18-15-46_2020-12-29T18-40-32.zip'

current_year = str(now.year)
city_path = 'Тюмень'

sborka_path = '//ewuk-adc02/CityShares/' + city_path + '/!Сборочка/' + current_year

cites = ['Tyumen', 'Tobolsk', 'Ivnono', 'Ryazan']
cites_ru = ['Тюмень', 'Тобольск', 'Иваново', 'Рязань']

print('Какой регион был выгружен?')
print('1 - Тюмень\n', '2 - Тобольск\n', '3 - Иваново\n', '4 - Рязань\n')

user_input = input()


def extract_archive(name, path):
    zipFile = zipfile.ZipFile(bases_path + file, 'r')
    zipFile.extract(cites[user_input] + '.dgdat', '//ewuk-adc02/CityShares/Тюмень/!Сборочки/2021/Январь/final/')
    zipFile.close()


if user_input == '1':
    print('Tyumen')
    city = 'Tyumen'
    print(sborka_path)

    # shutil.copy(bases_path, file)

    pass
elif user_input == '2':
    city = 'Tobolsk'
    pass
elif user_input == '3':
    pass
elif user_input == '4':
    city = 'Ryazan'
    pass

# end_file = 'c:/1/Tyumen.dgdat'
# file_size = os.path.getsize(path + file)
# print(file_size)

# zipFile = zipfile.ZipFile('C:/1/new.zip', 'r')
# zipFile.extract('1.txt', 'c:/1/')
# zipFile.close()

for i in trange(100):
    sleep(0.01)
