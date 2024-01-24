import os
import time
import pyaudio
import speech_recognition as sr
import playsound
from gtts import gTTS
import openai

api_key = "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"

lang = 'en'

openai.api_key = api_key


while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Friday" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome.mp3")
                    playsound.playsound("welcome.mp3")

            except Exception:
                print()

        return said



    get_audio()