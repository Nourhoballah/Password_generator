
import string
import random

### FRANÇAIS ###
# string est un module intégré de Python qui contient diverses constantes et fonctions
# pour manipuler des strings
# .ascii_letters est une constante du module string. Elle contient tous les caractères
# alphabétiques en minuscule et en majuscule

### ENGLISH ###
# string is a built-in Python module that contains various constants and functions
# to manipulate strings
# .ascii_letters is a constant from the string module. It contains all
# alphabetic characters in lowercase and uppercase

# Lettres minuscules / Lowercase letters
lower_letters = string.ascii_letters[0:26]  # Équivaut à string.ascii_lowercase / Equivalent to string.ascii_lowercase
random_lower_letters = random.sample(lower_letters, 3)  # .sample c'est sans répétition / .sample ensures no repetition

# Lettres majuscules / Uppercase letters
Upper_letters = string.ascii_letters[26:]  # Équivaut à string.ascii_uppercase / Equivalent to string.ascii_uppercase
random_upper_letters = random.sample(Upper_letters, 3)

# Caractères spéciaux / Special characters
possible_characters = "!@#$%&*?"
random_characters = random.sample(possible_characters, 3)

# Chiffres / Numbers
numbers = "0123456789"
random_numbers = random.sample(numbers, 3)

### FRANÇAIS ###
# Je fais .join car le code en haut donne une liste. Lorsque je join, j'ai un string.
### ENGLISH ###
# I use .join because the code above produces a list. By joining, I get a string.
password_list = random_numbers + random_upper_letters + random_lower_letters + random_characters

### FRANÇAIS ###
# random.shuffle permet de changer l'ordre des éléments dans mon mot de passe
### ENGLISH ###
# random.shuffle shuffles the order of the elements in the password
random.shuffle(password_list)
password_generator = "".join(password_list)

print(password_generator)

