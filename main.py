
import random
import requests

# Pokemon choices
pokemons = ["pikachu", "charmander", "bulbasaur", "squirtle", "eevee"]

# Choose a random Pokemon
pokemon = random.choice(pokemons)

try:
    # Get Pokemon data from API
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        print("=== WHO'S THAT POKEMON? ===")
        print("Height:", height)
        print("Weight:", weight)

        # Three attempts
        for i in range(3):
            guess = input("Guess the Pokemon: ").lower().strip()

            if guess == name:
                print("Correct! You win!")
                break
            elif guess not in pokemons:
                print("Invalid Pokemon name!")
            else:
                print("Wrong guess!")

        else:
            print("Game Over! The Pokemon was", name)

    else:
        print("Pokemon not found! HTTP status:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error! Please try again.")