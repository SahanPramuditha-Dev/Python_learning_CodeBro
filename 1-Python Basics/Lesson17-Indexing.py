credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[0])  
# Gets the character at index 0 → '1'

print(credit_card_number[:5])  
# From start up to (but not including 5th index) index 5 → '1234-' 0th index 1st index 2 3 4

print(credit_card_number[5:10])  
# Characters from index 5 to 9 → '5678-'

print(credit_card_number[10:15])  
# Characters from index 10 to 14 → '9012-'

print(credit_card_number[15:])  
# From index 15 to the end → '3456'

print(credit_card_number[-1:])  
# Last character only → '6'

print(credit_card_number[-4:])  
# Last 4 characters → '3456'

print(credit_card_number[::3])  
# Every 3rd character from start → '159-26'
# (Start at index 0, step = 3)

print(credit_card_number[::-1])  
# Reverses the string using step -1 → '6543-2109-8765-4321'

last_digits = credit_card_number[-4:]  
print(f"XXXX-XXXX-XXXX-{last_digits}")