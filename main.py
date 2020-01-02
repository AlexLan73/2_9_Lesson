# Спасибо за урок, узнал новые для себя вещи
import cmath
import datetime 
import collections
import re
import os
"""
Задание 1
Условие: Используя методы модуля cmath, найти значения  expj∗2πk/n  для всех целых  k  от  1  до  20  и  n=4  ( j  - мнимая единица). Найдите количество различных элементов при условии округления действительной и мнимой частей до целого.
Формат ответа: Число (например, 2)
Оценка в баллах: 2 балла

Решение:
"""
def L_1(n):
    z=2* cmath.pi/n
    for it in range(n):
        print(cmath.exp(z*it))


"""
Задание 2
Условие: Методами библиотеки datetime найти количество високосных годов 
с начала Unix эпохи и по настоящий момент.
"""
def L_2(year):
    ls_year = []
    i=0
    dt = datetime.datetime.now()
    dt_year = dt.year+1
    for item in  range(year, dt_year):
        if (item % 4 == 0) and (item % 100 != 0) or (item % 400 == 0):
            ls_year.append(item)
            i+=1
            print(item)
    return i, ls_year

"""
Задание 3
Условие: Перевести текст _Text_ в нижний регистр(str.lower), 
подсчитать статистику встречаемости символов(модуль collections), 
получить лист всех слов(модуль re). Найти количество слов, длина которых равна 6.
"""
def L_3():
    _Text_ = r'Представим, что какая-нибудь высокоразвитая цивилизация нашла быстровращающуюся чёрную дыру и построила вокруг неё сферическую оболочку из зеркал, обращённых внутрь. Оболочку сплошную, как каноническая сфера Дайсона. Благо, чёрные дыры намного меньше звёзд, так что и оболочку построить несравненно проще. Теперь открываем в ней отверстие и запускаем внутрь пучок электромагнитных волн. Эти волны получают с помощью эргосферы ускорение и вылетают наружу, отражаются от зеркала, возвращаются в эргосферу, ещё больше ускоряются, опять вылетают, отражаются, возвращаются, ускоряются, и т. д. (какая-то часть волн будет потеряна из-за падения на горизонт событий). Каждое попадание излучения в эргосферу приводит его экспоненциальному усилению. Это так называемый эффект рассеивания с помощью сверхизлучения, впервые предсказанный советским физиком Яковом Зельдовичем.'
    _text_low=_Text_.lower()    
#    print(_text_low)
    l_ch=list(_text_low)
    d_char = collections.defaultdict(int)
    for it_char in l_ch:
        d_char[it_char]+=1
#    print(d_char)
    print("-"*40)
    #_text_re = 
    _text_re =re.sub(r'[,.-]', '',  _text_low) #r'[,.-]'
    _text_re =re.sub(r'\(.+\)', '',  _text_re) #r'[,.-]'
    print(_text_re)
    _text_split=re.split(r' ', _text_re)
    print(_text_split)
    print("="*50)
    _text_6= re.findall(r'\b\w{6}\b',  _text_re)
    print(_text_6)

"""
Задание 4
Условие:
Методами модуля os cоставить статистику размера файлов *.csv папки sample_data из Google Colab. Составить словарь

size_dict = {'filename.csv':filename_size}
filename.csv - имя файла
filename_size - размер файла
Найти среднее значение длины файла, которое округлено до целого.
"""

def L_4():
    my_path= os.path.dirname(os.path.abspath(__file__))
    print("->", my_path)
    ls_dir=os.listdir()
    print(ls_dir) # "*.csv"
    ls1=[x for x in ls_dir if ".csv" in x]
    print(ls1) 
    d_file = collections.defaultdict(int)
    sum_size=0
    for item in ls1:
        size0 = os.path.getsize(item)
        sum_size+=size0
        print(item, size0)
        d_file[item]=size0
    sred = sum_size/ls1.__len__()
    print(d_file)       
    print("Среднее значение = {}".format(sred)) # 'Найти среднее значение длины файла, которое округлено до целого.' - Вроде это))
    

if __name__ == "__main__":
    L_1(12)
    k=1970
    i0, ls= L_2(k)
    print(" Начиная с {} по сегодня было {} высокосных лет ".format(k, i0))
    L_3()
    L_4()


