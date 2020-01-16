import requests


print (requests.__version__)
google= requests.get("https://raw.githubusercontent.com/yuhang5/CMPUT404/master/lab1/404lab1.py")
print(google)
