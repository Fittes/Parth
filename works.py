
Для начала давайте разберемся, что же действительно означает на первый взгляд непонятное слово — парсинг. 
Прежде всего это процесс сбора данных с последующей их обработкой и анализом. К этому способу прибегают, 
когда предстоит обработать большой массив информации, с которым сложно справиться вручную. 
Понятно, что программу, которая занимается парсингом, называют — парсер. С этим вроде бы разобрались.

#title==user(FULL)
    all_users = []

    return all_users
Для начала работы, установим 3 библиотеки Python.

pip install beautifulsoup4

Без цифры 4 вы ставите старый BS3, который работает только под Python(2.х).

pip install requests
pip install pandas

Теперь с помощью этих трех библиотек Python, можно проанализировать нашу веб-страницу.

Второй этап парсинга — Извлечение информации.

Попробуем получить структуру html-кода нашего сайта.
Давайте подключим наши новые библиотеки.

users= get_user('')

 all_users==views
 
for p in all_p:
 text = (p.text.strip() if len(p.text) >= 0 else "")
 if 'K' in text:
 text = str(float(text[:-1]) * 1000)
views.append(text)

Хорошо, мы получили названия вакансий. 
Давайте спарсим теперь каждую ссылку на вакансию и ее описание.
Описание находится в теге p с классом overflow. Ссылка находится все в том же элементе a.

all_users==date
for p in all_p:
text = (str(p).strip()[
str(p).strip().rfind('=') + 2:str(p).strip().rfind('=') + 19] if len(str(p)) >= 0 else "")
date.append(text)
Давайте соберем всю полученную информацию по страничке и запишем в удобный формат — json.

def build_json(result_file_path = 'result_test_parser.json'):
    result = dict()
    result['data'] = data
    result['views'] = views
    result['users'] = users
    result['title'] = title
    
    result_json = json.loads(json.dumps(result))
    
    with open(result_file_path, 'w', encoding='utf-8') as f:
        json.dump(result_json, f, ensure_ascii=False)
    
    return result_json


#import json
res_dict = build_json()

чтобы смореть результат пешите только имя 

Фрейм данных – это двухмерный набор данных, структура, в которой данные хранятся в табличной форме.
Наборы данных упорядочены по строкам и столбцам; мы можем хранить несколько наборов данных во фрейме данных. Мы можем выполнять 
различные арифметические операции, такие как добавление выбора столбца или строки и столбцов или строк во фрейме данных.


работаем с данными 

df_data = []
for i in range(len(res_dict['data'])):
    df_data.append([res_dict['data'][i], res_dict['views'][i], res_dict['users'][i], res_dict['title'][i]])
    
   ####так же никуда без импорта панды
df = pd.DataFrame(data=df_data, columns=['Дата', 'Просмотры', 'Пользователи', 'Тема'])
и смортим на результат
