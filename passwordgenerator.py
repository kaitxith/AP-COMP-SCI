import random

# procedure removes vowels
def remove_vowels(text, replacement_char=''):
    vowels = "aeiou"
    for vowel in vowels:
        text = text.replace(vowel, replacement_char)
    return text

# procedure to scramble letters
def scramble_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

# procedure change odd digits and zeros to random symbols
def change_odd_0_to_symbols(text):
    result = ""
    symbols = "!@#$%^&*"
    for char in text:
        if char.isdigit():
            if int(char) % 2 == 1 or char == '0':
                result += random.choice(symbols)
            else:
                result += char
        else:
            result += char
    return result

# generate password
def generate_password(website, randomword, dob):
    
    website = remove_vowels(website)
    
    randomword = scramble_text(randomword)
    
    dob = change_odd_0_to_symbols(dob)
    
    password = f"{website}{randomword}{dob}"
    
    return password

# main stuff
if __name__ == "__main__":
    website = input("Enter the website you use: ")
    randomword = input("Enter a random word, gibberish, or what you're using the website for: ")
    dob = input("Enter your date of birth (in MMDDYYYY): ")
    
    password = generate_password(website, randomword, dob)
    
    print(f"Your password for {website} is: {password}")