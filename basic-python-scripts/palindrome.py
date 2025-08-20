# Palindrome Checker

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    test_word = "madam"
    print(f"Is '{test_word}' a palindrome?", is_palindrome(test_word))
