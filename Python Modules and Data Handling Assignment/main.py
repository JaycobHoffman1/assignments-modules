import mood_responses

# Task 1: Your Mood Today

def main():
    while True:
        try:
            mood_input = input("How are you feeling today?: ")

            if (not mood_input) or len(mood_input) == mood_input.count(" "):
                raise ValueError("Input cannot be blank.")
        except ValueError as v:
            print(v)
        else:
            break

    mood_responses.mood_response(mood_input)

if __name__ == "__main__":
    main()