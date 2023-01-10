import requests
print(requests.__version__)
print(requests.get("http://google.com/"))
script = requests.get("https://raw.githubusercontent.com/ashutoshlamba/404lab1/main/script.py")
print(script.text)
