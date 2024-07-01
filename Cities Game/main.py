import random,pandas,csv

from bs4 import BeautifulSoup
import lxml,requests,unicodedata


class CityGame:
    def __init__(self):
        self.get_data()
        self.game_works = True
        name = input("Welcome to the city game.What is your name?\n")
        print(f"Hello {name} good luck!")
        self.play()

    def get_data(self):
        self.df = pandas.read_csv("worldcities.csv")

        self.cities = []
        self.real_city_names = []
        self.country_list = []
        self.populations = []
        for (index, row) in self.df.iterrows():
            self.cities.append(row["city_ascii"])
            self.real_city_names.append(row["city"])
            self.country_list.append(row["country"])
            self.populations.append(row["population"])

    def play(self):
        while self.game_works:
            city = input("Enter a city")
            if city in self.cities:
                index = self.cities.index(city)
                real_name = self.real_city_names[index]
                country = self.country_list[index]
                population = self.populations[index]
                last_letter_user = city[-1].lower()
                print(last_letter_user)
                if city == real_name:
                    print(f"{city}, {country} with population:{population}\nThe last letter was {last_letter_user}")
                    print(f"https://en.wikipedia.org/wiki/{city}")
                else:
                    print(f"{city}, {country} ({real_name}) with population:{population}\nThe last letter was {last_letter_user}")
                    print(f"https://en.wikipedia.org/wiki/{city}")

                self.cities.pop(index)
                self.real_city_names.pop(index)
                self.country_list.pop(index)
                self.populations.pop(index)
                choices = [c for c in self.cities if c[0].lower() == last_letter_user]
                if len(choices) == 0:
                    game_works = False
                    print("You won")
                else:
                    city_chosen = random.choice(choices)
                    last_letter = city_chosen[-1].lower()
                    index = self.cities.index(city_chosen)
                    real_name = self.real_city_names[index]
                    country = self.country_list[index]
                    population = self.populations[index]

                    self.cities.pop(index)
                    self.country_list.pop(index)
                    self.populations.pop(index)
                    self.real_city_names.pop(index)
                    if city_chosen != real_name:
                        print(f"{city_chosen}, {country} ({real_name})with population:{population}\nThe last letter is {last_letter}")
                        print(f"https://en.wikipedia.org/wiki/{city_chosen}")
                    else:
                        print(
                            f"{city_chosen}, {country} with population:{population}\nThe last letter is {last_letter}")
                        print(f"https://en.wikipedia.org/wiki/{city_chosen}")
            else:
                if_quit = input("x to quit")
                if if_quit == "x":
                    self.game_works = False

if __name__ == "__main__":
    cg = CityGame()