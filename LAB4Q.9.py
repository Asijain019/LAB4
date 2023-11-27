sentence = input("Enter a sentence: ")

# Initialize counters
capital_count = 0
small_count = 0
digit_count = 0
special_count = 0

# Iterate through each character in the sentence
index = 0
while index < len(sentence):
    char = sentence[index]

    # Check if the character is a capital letter
    if 'A' <= char <= 'Z':
        capital_count += 1
    # Check if the character is a small letter
    elif 'a' <= char <= 'z':
        small_count += 1
    # Check if the character is a digit
    elif '0' <= char <= '9':
        digit_count += 1
    # If it's not a letter or digit, consider it as a special character
    else:
        special_count += 1

    # Move to the next character
    index += 1

# Print the results
print("Capital letters:", capital_count)
print("Small letters:", small_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
