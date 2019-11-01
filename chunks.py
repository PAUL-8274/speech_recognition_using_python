import speech_recognition as sr
r = sr.Recognizer()
audio=input()
sound = sr.AudioFile(audio)

with sound as source:
    audio1 = r.record(source,offset=4,duration=4)
    audio2 = r.record(source,offset=4,duration=4)
type(audio1)
type(audio2)  
r.recognize_google(audio1)
r.recognize_google(audio2)
text1=r.recognize_google(audio1)
text2=r.recognize_google(audio2)
print(text1)
print(text2)
print(text1+ " " + text2)
