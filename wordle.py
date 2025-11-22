import requests

data = requests.get("https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt")
with open("words.txt", "w") as f:
    f.write(data.text)
    print("data written successfully.")
    print("run main.py to play the wordle game.")
