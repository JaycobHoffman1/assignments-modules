import re as r

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def remove_vowels(s): # Excludes "y"
    return r.sub(r"[AEIOUaeiou]", "", s) if r.search(r"[AEIOUaeiou]", s) else "No vowels to remove!"