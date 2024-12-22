def is_palindrome(word):
    if isinstance(word, int):
        return str(word) == str(word)[::-1]
    elif isinstance(word, str) or isinstance(word, tuple) or isinstance(word, list):
        return word == word[::-1]