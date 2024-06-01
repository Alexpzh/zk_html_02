import requests
import pprint

def test1():
    url = 'https://api.github.com/search/repositories'
    param = {
        'q': 'html'
    }

    response = requests.get(url, params=param)
    response_json = response.json()
    with open("test1.txt", "w") as f:
        f.write(f"Статус кода ответа = {response.status_code}\n")
        f.write(f"Найдено по запросу html = {response_json['total_count']}\n")
        response_json['total_count']
        #f.write(str(response_json))
        pprint.pprint(response_json, f)
        f.close()

test1()


# url = 'https://api.github.com/search/repositories'
#
# param = {
#     'q' : 'C++'
# }
#
# response = requests.get(url, params = param)
# print(response.status_code)
# print(response.ok)
# if response.ok:
#     print (response.text)
#
# response_json = response.json()
# pprint.pprint(response_json)
#
#
# print(response_json['total_count'])