def is_valid_tag(tag):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    
    # Extracting digits and letter
    d1, d2, letter, d3, d4, d5, sep, d6, d7 = tag

    # Check if the letter is a vowel
    if letter in vowels:
        return "invalid"
    
    # Check if the separator is '-'
    if sep != '-':
        return "invalid"

    # Convert digits to integers
    d1, d2, d3, d4, d5, d6, d7 = map(int, [d1, d2, d3, d4, d5, d6, d7])

    # Check if the sum of consecutive digits is even
    if (d1 + d2) % 2 != 0 or (d3 + d4) % 2 != 0 or (d4 + d5) % 2 != 0 or (d6 + d7) % 2 != 0:
        return "invalid"
    
    return "valid"

# Taking input
tag = input().strip()

# Checking and printing the result
print(is_valid_tag(tag))
