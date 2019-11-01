import speech_recognition as sr
r = sr.Recognizer()
audio=input("file=")
sound = sr.AudioFile(audio)
with sound as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
#r.recognize_google(audio)

lis=r.recognize_google(audio, show_all=True)

print(lis)
