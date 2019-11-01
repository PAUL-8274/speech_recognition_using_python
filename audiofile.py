import speech_recognition as sr
r = sr.Recognizer()
audio=input() #type examples/hindi_04.wav
sound = sr.AudioFile(audio)
with sound as source:
    audio = r.record(source)

try:
    print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
except:                                 # speech is unintelligible
    print("Could not understand audio")

