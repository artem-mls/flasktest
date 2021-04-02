from requests import get, post, delete

# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/v2/users',
#            json={'about': 'Жеребёнок',
#                  'name': 'Человек',
#                  'email': 'zherebyonok@zh.ru',
#                  'hashed_password': '123'}).json())

# print(get('http://localhost:5000/api/v2/users').json())

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/v2/users/5').json())
