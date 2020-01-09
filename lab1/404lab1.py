import requests


print (requests.__version__)
google= requests.get("https://www.google.com")
print(google)
