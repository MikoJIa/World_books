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

import math


def series_sum(n):
    res = 0
    if n <= 1:
        return "{:.2f}".format(n)
    if n > 1:
        for i in range(n):
            res += 1 / (3 * i + 1)
        return str("{:.2f}".format(res))


print(series_sum(5))