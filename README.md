# CLI Password Generator

This is a simple command-line interface (CLI) password generator written in Python. The script generates secure random passwords that include numbers, lowercase letters, capital letters, and common symbols by default. The length of the password can be specified as a command-line argument.

## Requirements

- Python 3.6+

## Usage

To use the script, open a terminal or command prompt and navigate to the directory where the `password_generator.py` file is located. Then, run the script using the following command:
```
python password_generator.py
```


By default, the script generates a 12-character password that includes numbers, lowercase letters, capital letters, and common symbols.

To generate a password of a different length, specify the length as a command-line argument using the `-l` or `--length` option:
```
python password_generator.py -l 16
```


This generates a 16-character password.

## Notes

This script uses the `secrets` module to generate secure random passwords. The `secrets` module uses a cryptographically secure random number generator and is specifically designed for generating random values that need to be secret (like passwords).
