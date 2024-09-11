import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Rastgele harfleri, sembolleri ve sayıları seçmek
random_letters = random.choices(letters, k=nr_letters)
random_symbols = random.choices(symbols, k=nr_symbols)
random_numbers = random.choices(numbers, k=nr_numbers)

# Şifreyi birleştirmek
password_list = random_letters + random_symbols + random_numbers

# Şifreyi karıştırmak
random.shuffle(password_list)

# Şifreyi stringe dönüştürmek
password = ''.join(password_list)

print("Your password is:")
print(password)
