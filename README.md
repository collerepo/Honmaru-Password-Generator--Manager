Honmaru Password Generator & Manager
============================================================

This script generates strong, unique passwords and stores them securely. It also provides options to retrieve and delete passwords.

//Note: Make sure to use the 'StrongPasswordGeneratorV3.py' file as it is the latest and most complete version of the final product. DO NOT use the 'test' version as it is outdated and was meant as a trial for the final version.

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
MIT License

Copyright (c) 2024 Rodrigo Coll

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
