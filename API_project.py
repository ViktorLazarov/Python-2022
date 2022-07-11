import requests
import random
import pyfiglet
import termcolor

header = pyfiglet.figlet_format("DAD JOKES 2000")
header = termcolor.colored(header, color='red')
print(header)

user_input = input("Enter search parameter!: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}).json()

num_jokes = res['total_jokes']
if num_jokes > 1:
    print(f"I've found {num_jokes} jokes with the word {user_input}. Here's one!")
    joke = random.choice(res['results'])['joke']
    print(joke)
elif num_jokes == 1:
    print(f"There is only one joke with the word {user_input}")
    print(res['results'][0]['joke'])
else:
    print(f"There are no jokes with the word {user_input}")
