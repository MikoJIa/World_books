# import requests
# import json
#
# url = "https://reqres.in/api/users"
#
# payload = json.dumps({
#   "name": "Nikolay",
#   "job": "Programmer"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)


def reverse_words(text):
    new_text = []
    for item in text.split(' '):
        new_text.append(item[::-1])
    return ' '.join(new_text)


print(reverse_words('double  spaced  words'))