from gtts import gTTS
import os
import speech_recognition as sr
from openai import Client

client = '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'

def send_message(message_log):
    completion = client.chat.completions.create(
        model="text-davinci-003",
        messages=[
            {"role": "user", "content": message_log}
        ]
    )
    return completion.choices[0].message.content

def tts(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            user_input = r.recognize_google(audio)
            print(f"You: {user_input}")
            return user_input
        except Exception as e:
            print("Error: ", str(e))
            return ""

def main():
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    first_request = True
    
    while True:
        if first_request:
            user_input = stt()
            first_request = False
        else:
            user_input = input("You: ")
        
        response = send_message(user_input)
        
        print(f"AI assistant: {response}")
        
        tts(response)

if __name__ == "__main":
    main()
    