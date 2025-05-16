# interface/voice_input.py

import speech_recognition as sr

def listen_for_prompt() -> str:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Listening... Speak your prompt:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        prompt = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Speech Recognition error: {e}")
        return ""
