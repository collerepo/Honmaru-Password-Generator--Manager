Password Generator and Manager
============================================================

This script generates strong, unique passwords and stores them securely. It also provides options to retrieve and delete passwords.

*******Usage********
-----

1. Run the script and follow the prompts to generate a password.
2. The password will be stored securely in the `passwords.txt` file.
3. To retrieve a password, run the script and select the "Retrieve password" option.
4. To delete a password, run the script and select the "Delete password" option.

******Security******
--------

The script uses the `secrets` module to generate cryptographically secure random numbers. Passwords are stored using the `hashlib` library with a salt value to prevent rainbow table attacks.

******License*******
-------

This script is licensed under the MIT License.
