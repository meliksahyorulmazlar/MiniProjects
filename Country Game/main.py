#Country game
#The game starts with the computer choosing a random letter.The country it will choose will start that random letter.
#Let's say the computer chose r , it will find all the countries that start with r. Let's say it randomly chose Russia
#Then the user has to enter a country that starts with a and the user can go with australia
#If its someone's turn and there are no countries remaining to say starting with that letter, that person loses the game and the other person wins the game
#example lets say person1 said uruguay,person 2 said yemen and person 1 said norway.There are no countries starting with y starting therefore person1 won the game
#the final rule is a country cant be said twice so if russia was already said, you can't say russia later on in the game
import random


class CountryGame:
    def __init__(self):
        self.countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua And Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia And Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cape Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Congo", "Congo", "Comoros", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria","North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts And Nevis", "Saint Lucia", "Saint Vincent And The Grenadines", "Samoa", "San Marino", "Sao Tome And Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa","South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor Leste", "Togo", "Tonga", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
        self.game_works = True
        self.you_won = False
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'z']
        #I deleted w,x because no country starts with w or x
        self.letters = [l.upper() for l in self.letters]
        self.play()

    def find_country(self,letter:str):
        letter = letter.upper()
        countries_found = []
        for country in self.countries:
            if country[0] == letter:
                countries_found.append(country)
        if len(countries_found) == 0:
            self.you_won = True
            self.game_works = False
            print("No country found")
        else:
            #print(countries_found)
            country_chosen = random.choice(countries_found)
            self.countries.remove(country_chosen)
            self.last_letter = country_chosen[-1].upper()
            check_remaining = [c for c in self.countries if c[0] == self.last_letter]
            if len(check_remaining) == 0:
                print(country_chosen)
                self.you_won = False
                self.game_works = False
            else:
                print(country_chosen)

    def start_game(self):
        print("Welcome to the country game")
        name = input("What is your name?\n")
        print(f"Hello {name} good luck in the game!")
        letter_chosen = random.choice(self.letters)
        self.find_country(letter=letter_chosen)

    def play(self):
        self.start_game()
        while self.game_works:
            print(f'{self.last_letter} is the last letter')
            country = input('Enter a country').title()
            if country in self.countries and country[0] == self.last_letter:
                self.last_letter = country[-1].upper()
                self.countries.remove(country)
                self.find_country(letter=self.last_letter.upper())



        if self.you_won:
            print("You won")
        else:
            print("You lost")



if __name__ == "__main__":
    cg = CountryGame()
