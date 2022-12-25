# Password generator 

import random 
import array

# the format will be : 4 sequences that will include numbers, 
# letters and symbols and will be
# divided by 3 _ (underscore)

# ex: kSfw@2_sPDf#0_vBqw*4_ahoT4}

# Every sequence will be 6 characters long
MAX_len1 = 6
MAX_len2 = 6
MAX_len3 = 6
MAX_len4 = 6


# Creating a list for every type of value that we can 
# put into the password
digits = ['0','1','2','3','4','5','6','7','8','9']

lowcase_char = ['a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t'
                'u','v','w','x','y','z']

upcase_char = ['A','B','C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R','S','T'
                'U','V','W','X','Y','Z']

symbols = ['@','#','$','%','^','&','*','(',')','-','=',
           '+','/','|','[',']','{','}',':',';','.',',',
           '>','<']

# Creating a combined list so we can choose from it a lot easier
combined_list = digits + lowcase_char + upcase_char + symbols

# Since there will be 4 sequences, we create 4 different
# Randomly chosen value from each list to eliminate repetition
rand_digit1 = random.choice(digits)
rand_lower1 = random.choice(lowcase_char)
rand_upper1 = random.choice(upcase_char)
rand_symbols1 = random.choice(symbols)

rand_digit2 = random.choice(digits)
rand_lower2 = random.choice(lowcase_char)
rand_upper2 = random.choice(upcase_char)
rand_symbols2 = random.choice(symbols)

rand_digit3 = random.choice(digits)
rand_lower3 = random.choice(lowcase_char)
rand_upper3 = random.choice(upcase_char)
rand_symbols3 = random.choice(symbols)

rand_digit4 = random.choice(digits)
rand_lower4 = random.choice(lowcase_char)
rand_upper4 = random.choice(upcase_char)
rand_symbols4 = random.choice(symbols)

# Creating temporary passwords so that we make
# sure that every value from the lists is 
# included in the password
temp_password1 = rand_digit1 + rand_lower1 + rand_upper1 + rand_symbols1
temp_password2 = rand_digit2 + rand_lower2 + rand_upper2 + rand_symbols2
temp_password3 = rand_digit3 + rand_lower3 + rand_upper3 + rand_symbols3
temp_password4 = rand_digit4 + rand_lower4 + rand_upper4 + rand_symbols4


# Creating a for loop for every temporary password
# So that we can add missing 2 values from the combined list
for i in range(MAX_len1 - 4):
    temp_password1 = temp_password1 + random.choice(combined_list)


    temp_password1_list = array.array('u', temp_password1)
    random.shuffle(temp_password1_list)

for i in range(MAX_len2 - 4):
    temp_password2 = temp_password2 + random.choice(combined_list)


    temp_password2_list = array.array('u', temp_password2)
    random.shuffle(temp_password2_list)

for i in range(MAX_len3 - 4):
    temp_password3 = temp_password3 + random.choice(combined_list)


    temp_password3_list = array.array('u', temp_password3)
    random.shuffle(temp_password3_list)

for i in range(MAX_len4 - 4):
    temp_password4 = temp_password4 + random.choice(combined_list)


    temp_password4_list = array.array('u', temp_password4)
    random.shuffle(temp_password4_list)


# After the shuffling is completed, we create the new passwords
password1 = ""
password2 = ""
password3 = ""
password4 = ""

for i in temp_password1_list:
    password1 = password1 + i

for i in temp_password2_list:
    password2 = password2 + i

for i in temp_password3_list:
    password3 = password3 + i

for i in temp_password4_list:
    password4 = password4 + i

# Creating the actual password with the concatenation method
print(password1 + '_' + password2 + '_' + password3 + '_' + password4)
