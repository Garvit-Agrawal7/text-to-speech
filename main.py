import pyttsx3
from pypdf import PdfReader

engine = pyttsx3.init()

pdf = input("Enter the relative path to the PDF file: ")
reader = PdfReader(pdf)

rate = engine.getProperty('rate')
engine.setProperty('rate', 250)    # Change the value to increase or decrease speed, default is 200

# engine.setProperty('volume', 1)   # Change volume, value range, 0 - 1

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)    # Male voice
# engine.setProperty('voice', voices[1].id)   # Female voice

for page in reader.pages:
    engine.say(page.extract_text())

    engine.save_to_file(page.extract_text(), f'Page {reader.pages.index(page)+1}.mp3')
    engine.runAndWait()
    engine.stop()
