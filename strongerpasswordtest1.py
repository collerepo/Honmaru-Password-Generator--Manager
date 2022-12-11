import random
import array

MIN_LEN = 8
MAX_LEN = 512

randvars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
         '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29',
         '30', '31', '32', '33', '34', '35', '36', '37', '38',
         '39','40', '41', '42', '43', '44', '45', '46', '47',
         '48', '49', '50', '51', '52', '53' '54', '55', '56',
         '57', '58', '59', '60', '61', '62', '63', '64', '65',
         '66', '67', '68', '69', '70', '71', '72', '73', '74',
         '75', '76', '77', '78', '79', '80', '81', '82', '83',
         '84', '85', '86', '87', '88', '89', '90', '91', '92',
         '93', '94', '95', '96', '97', '98', '99', 'a', 'b',
         'c', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg',
         'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq',
         'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', '!', '@',
         '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', ',', '.',
         '{', '}', '/', '|', '~', '`', '<', '>', '==', '!=', '&&', '**']

numerical_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
         '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29',
         '30', '31', '32', '33', '34', '35', '36', '37', '38',
         '39','40', '41', '42', '43', '44', '45', '46', '47',
         '48', '49', '50', '51', '52', '53', '54', '55', '56',
         '57', '58', '59', '60', '61', '62', '63', '64', '65',
         '66', '67', '68', '69', '70', '71', '72', '73', '74',
         '75', '76', '77', '78', '79', '80', '81', '82', '83',
         '84', '85', '86', '87', '88', '89', '90', '91', '92',
         '93', '94', '95', '96', '97', '98', '99']

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
           '[', ']', '{', '}', ';', ':', '"', '?', '<', '>', '`', '~', '|', '/']

# combine all the character arrays above to form one array

combined_list = randvars + numerical_digits + lowercase_letters + uppercase_letters + symbols

# randomly select a least one character from each character set above
rand_variable = random.choice(randvars)
rand_digits = random.choice(numerical_digits)
rand_lower = random.choice(lowercase_letters)
rand_upper = random.choice(uppercase_letters)
rand_symbol = random.choice(symbols)

# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password

temporary_password = rand_variable + rand_digits + rand_lower + rand_upper + rand_symbol

# Now we can be sure that we have at least one character from each set
# of the characters of the list generated above from the various arrays
# let us now fill the remaining the password length by selecting randomly
# from the combined list of the character above:


for x in range(MAX_LEN - 4):
    temporary_password = temporary_password + random.choice(randvars)

    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temporary_password_list = array.array('u', temporary_password)
    random.shuffle(temporary_password_list)

# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temporary_password_list:
    password = password + x

# print out the password
print(password)

# declaring the empty string
password = ""

# loop to generate the random password of thr length entered by the user
for x in range(512):
     password = password + random.choice(randvars)[0]

print('Your New Password is:\n', password)

