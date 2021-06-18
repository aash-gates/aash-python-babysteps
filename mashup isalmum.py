#Program to check if the string value is composed of digits and/or letters or both IBM Digital Nation

only_digits ="1234567890"
print(only_digits.isalnum()) #returns True

import time
time.sleep(1.00)

only_letters ="aash"
print(only_letters.isalnum()) #returns true

import time
time.sleep(1.00)


has_digit ="8954@"
print(has_digit.isalnum()) #returns False

has_letters = "aash"
print(has_letters.isalnum()) #returns true

has_digit_letters = "12mn3"
print(has_digit_letters.isalnum()) #returns True

no_digit_letters = "@@$&&*##"
print(no_digit_letters.isalnum()) #returns false