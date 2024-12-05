import requests

# создание объявления
# response = requests.post(
#     "http://127.0.0.1:5000/ad",
#     json={
#         "header": "ad_3",
#         "description": "description_3",
#         "owner": "owner_2"
#     }
# )
# print(response.status_code, response.json())



#обновление объявления
# response = requests.patch(
#     "http://127.0.0.1:5000/ad/1",
#     json={
#         "header": "new_ad",
#     }
# )
#print(response.status_code, response.json())



# получение объявления
# response = requests.get(
#     "http://127.0.0.1:5000/ad/7",
# )
# print(response.status_code, response.json())



#удаление объявления
# response = requests.delete(
#     "http://127.0.0.1:5000/ad/1",
# )
# print(response.status_code, response.json())
# response = requests.get(
#     "http://127.0.0.1:5000/ad/1",
# )
# print(response.status_code, response.json())