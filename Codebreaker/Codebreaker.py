# The corrupted satellite data feed
satellite_feed = [
    "72-69-76-76-79",       # Encrypted Word 1 (ASCII decimal codes)
    "87-79-82-76-68",       # Encrypted Word 2 (ASCII decimal codes)
    42,                     # Corrupted data!
    "  _sYstEm_oNlInE_  ", # System status string
    "0"                     # Battery critical override multiplier
]

# Task 1: Characters & Strings vs. Computers

def decode_ascii(encoded_string):
    """
    Takes a dash-separated ASCII decimal string like "72-69-76-76-79"
    Splits it, converts each number to a character, joins into a word.
    """
    # Step 1: Split the string by dashes → ["72", "69", "76", "76", "79"]
    number_strings = encoded_string.split("-")

    # Step 2: Convert each string number → integer → ASCII character
    characters = []
    for num_str in number_strings:
        number    = int(num_str)       # "72"  → 72
        character = chr(number)        # 72   → 'H'
        characters.append(character)

    # Step 3: Glue all characters into one word
    word = "".join(characters)
    return word


# Decode the first two items
word1 = decode_ascii(satellite_feed[0])   # "72-69-76-76-79"
word2 = decode_ascii(satellite_feed[1])   # "87-79-82-76-68"

print("Decoded Word 1:", word1)   # → HELLO
print("Decoded Word 2:", word2)   # → WORLD

# Task 2: String Cleanup

# The messy 4th item (index 3)
raw_status = satellite_feed[3]    # "  _sYstEm_oNlInE_  "

# Step 1: Strip leading and trailing whitespace
step1 = raw_status.strip()        # "_sYstEm_oNlInE_"

# Step 2: Remove underscores by replacing them with space
step2 = step1.replace("_", " ")        # "sYstEm oNlInE"  ← underscores removed

# Step 3: Convert to lowercase
step3 = step2.lower()     # "system online"

print(f"Cleaned Status: {step3}")
 

# # Task 3: The Crash Test (No Error Handling)
# print("\nTask 3: The Crash Test (No Error Handling)")
# print("-----------------------------------")

# #  WARNING: This code will CRASH intentionally — Task 3 demonstration

# for item in satellite_feed:
#     result = decode_ascii(item)    # Will explode on item 42 (the integer)
#     print("Decoded:", result)
    
# Task 4: The Bulletproof Shield 

def decode_ascii(encoded_string):
    """Decodes a dash-separated ASCII string into a word."""
    number_strings = encoded_string.split("-")
    characters     = [chr(int(n)) for n in number_strings]
    return "".join(characters)

for index, item in enumerate(satellite_feed):

    if index == 4:                      # ← Target item 4 ("0") specifically
        try:
            result = 100 / int(item)
            print(f"   Override result: {result}")

        except ZeroDivisionError:
            print("  [SYSTEM WARNING]: Cannot divide by zero override.")


