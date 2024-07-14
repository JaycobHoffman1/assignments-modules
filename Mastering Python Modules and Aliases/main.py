import text_utils as t

# Task 1: Custom Module with Aliases

def main():
    string1 = "hello world!"
    string2 = "rhythm"
    reversed_string1 = t.reverse_string(string1)
    caps_string1 = t.capitalize_string(string1)
    cons_string1 = t.remove_vowels(string1)
    cons_string2 = t.remove_vowels(string2)

    print(f"\"{string1}\" in reverse:\n{reversed_string1}\n")
    print(f"\"{string1}\" capitalized:\n{caps_string1}\n")
    print(f"\"{string1}\" without vowels:\n{cons_string1}\n")
    print(f"\"{string2}\" without vowels:\n{cons_string2}")

if __name__ == "__main__":
    main()