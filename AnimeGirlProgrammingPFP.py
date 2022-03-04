import requests
import random
import base64

user = "cat-milk"
repo = "Anime-Girls-Holding-Programming-Books"

def getAnimuGirlPath():
    res = requests.get("https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(user, repo)).json()
    length = len(res["tree"])
    fileName = res["tree"][random.randint(0, length)]["path"]

    print("Using {} as our target profile picture.".format(fileName))
    return fileName

def pathToBase64(path):
    file = "https://raw.githubusercontent.com/{}/{}/master/{}".format(user, repo, path)
    return "data:image/png;base64," + base64.b64encode(requests.get(file).content).decode("utf-8")

def patchDiscordRequest(image, authorization):
    patchHeaders = {'Authorization': authorization}
    result = requests.patch("https://discord.com/api/v9/users/@me", json = {'avatar': image }, headers = patchHeaders)

    if result.status_code == 200:
        print("Successfully switched profile picture! Enjoy your programming book.")
    else:
        print("An unknown error occurred, truly unfortunate...")

image = pathToBase64(getAnimuGirlPath())
patchDiscordRequest(image, "Your Authorization Token")
