def mood_response(mood):
    moods = {
        "happy": "That's great to hear! I feel happy too!",
        "sad": "I'm so sorry to hear you are sad. Would you like to talk about it?",
        "angry": "If you are feeling angry, try taking a deep breath and counting to 10.",
        "excited": "Oooh! What are you excited about?",
        "anxious": "I'm sorry to hear you are feeling anxious. What are you feeling anxious about?"
    }

    try:
        for mood_key in moods.keys():
            if mood_key in mood.lower():
                print(moods[mood_key])

                return
            
        raise ValueError("I'm sorry, but I don't understand what you're saying.")
    except ValueError as v:
        print(v)