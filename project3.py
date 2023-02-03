
"""
1. Парсинг данных из файла в словарь:
employee = {
    NAME: 'Name'
    LAST_NAME: 'Last_name'
    TEL: '1111111'
    CITY: 'City'
    EMAIL: ''
}
2. Выбор валидных данных
3. Генерация почты
4. Генерация пароля
5. Добавление почты в данные файла
6. Запись файлов
"""

all_employees = {}
valid_data = []
not_valid_data = []
ID = []
user_id = 0

with open(r'/content/drive/MyDrive/Python/task_file.txt', 'r', encoding='utf-8') as file:
  file.readline() #пропускаем строку с заголовками
  for line in file:
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    data = line[1:].split(',') #['Ivan', 'Abramov', '7776514', 'Moscow']

    #dividing data
    name = data[0]
    last_name = data[1]
    tel = data[2]
    city = data[3]

    employee = {
        'NAME': name,
        'LAST_NAME': last_name,
        'TEL': tel,
        'CITY': city,
        'EMAIL': '',
        'PASSWORD': ''
        }   

    # data validation
    if name.istitle() and last_name.istitle() and len(tel) == 7 and tel.isdigit() and city.istitle():
      ID.append(user_id)
      valid_data.append([name, last_name, tel, city])
    else:
      not_valid_data.append([name, last_name, tel, city])
    user_id += 1

# emails generating
def email_gen(list_of_names):
  """Function generates e-mails out of given name and surname

    Example:
    print(email_gen(['Ivan', 'Petrov'], ['Ivan', 'Petrov'], ['Ivan', 'Petrov']))
    ['Petrov.I@company.io', 'Petrov.Iv@company.io', 'Petrov.Iva@company.io']

    Args:
    list of lists with names and surnames

    Returns:
    List of emails
  """ 
  emails = []
  for i in valid_data:
    letter = 1
    while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
      letter+=1
    emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
  return emails

def password_generator(list_of_names):
  """Function generate passwords

  Args:list of lists with names and surnames

  Returns:
  12-letter email from symbols '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

  """
  import random
  chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  passwords=[]  
  length = 12
  for n in range(len(valid_data)):
      password =''
      for i in range(length):
          password += random.choice(chars)
      passwords.append(password)
  return passwords

# adding emails and passwords to data
emails = email_gen(valid_data)
passwords = password_generator(valid_data)

for i in range(len(valid_data)):
  valid_data[i].insert(4, emails[i])
  valid_data[i].insert(5, passwords[i])

# saving data
with open(r'/content/drive/MyDrive/Python/project/result_file.txt', 'w', encoding='utf-8') as final:
  final.write('NAME, LAST_NAME, TEL, CITY, EMAIL, PASSWORD\n')
  for i in range(len(valid_data)):
    element = valid_data[i]
    line = ' , '.join(element)
    final.write(line +'\n')

with open(r'/content/drive/MyDrive/Python/project/result2_file.txt', 'w', encoding='utf-8') as final2:
  final2.write('NAME, LAST_NAME, TEL, CITY\n')
  for i in range(len(not_valid_data)):
    line = f"{not_valid_data[i]}\n"
    final2.write(line)