import urllib.request
import json
url = "https://official-joke-api.appspot.com/jokes/programming/random"

def get_joke():
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    setup = response_data[0]['setup']
    punchline = response_data[0]['punchline']
    joke = tuple([setup,punchline])
    print(joke)
    return joke

if __name__ == "__main__":
    get_joke()