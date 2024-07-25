import speech_recognition as sr
import random


mic = sr.Microphone()
recog = sr.Recognizer()

levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):

    if level not in levels:
        print("Invalid level.")
        return
    
 
    word_to_speak = random.choice(levels[level])
    print(f"Say the word: {word_to_speak}")
    

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
    
    user_input = recog.recognize_google(audio, language="en-US")
    print(f"You said: {user_input}")

    if user_input.lower() == word_to_speak.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False
    



if __name__ == "__main__":
    chosen_level = input("Choose level: easy, medium, hard: ").lower()
    score = 0
    while True:
        if play_game(chosen_level):
            score += 1
        else:
            score -= 1
