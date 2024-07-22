import os
import cv2
import pyttsx3
import pytesseract	
from PIL import Image	

def ttstext():
    # Recognize text in the image
    text = input("Input the words to say out loud\n>> ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)

    # Say the text out loud
    engine.say(text)
    engine.runAndWait()

def ttsimage():
    print("Make sure the file is already in place")

    image = Image.open('image.png').convert('L')

    # Recognize text in the image
    text = pytesseract.image_to_string(image).replace("\n", " ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)

    # Say the text out loud
    engine.say(text)
    engine.runAndWait()

def ttsfile():
    print("Make sure the file is already in place")

    file = open("file.txt","r")
    text = file.read().replace("\n"," ")    

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)

    # Say the text out loud
    engine.say(text)
    engine.runAndWait()

def ttscamera():
    # Start the webcam
    cap = cv2.VideoCapture(1)

    # Keep webcam open until s is pressed
    while True:
        _,image=cap.read()
        cv2.imshow("Press s to capture", image)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite('test.jpg' , image)
            break

    # Close webcam
    cap.release()
    cv2.destroyAllWindows()

    # Open the image
    image = Image.open('test.jpg').convert('L')

    # Recognize text in the image
    text = pytesseract.image_to_string(image).replace("\n", " ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)

    # Say the text out loud and print it
    print(text)
    engine.say(text)
    engine.runAndWait()

while(True):
    os.system('cls')
    print("1. Input manually")
    print("2. Image")
    print("3. txt file")
    print("4. Camera")
    print("0. Close program")
    option = int(input("Choose the tts source\n>> "))

    match option:
        case 1:
            os.system('cls')
            ttstext()
            input("\nPress Enter to continue...")
            os.system('cls')

        case 2:
            os.system('cls')
            ttsimage()
            input("\nPress Enter to continue...")
            os.system('cls')

        case 3:
            os.system('cls')
            ttsfile()
            input("\nPress Enter to continue...")
            os.system('cls')
        
        case 4:
            os.system('cls')
            ttscamera()
            input("\nPress Enter to continue...")
            os.system('cls')

        case 0:
            os.system('cls')
            print("Thankyou for using the app!")

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty("voice", voices[1].id)

            # Say the text out loud
            engine.say("Thankyou for using the app")
            engine.runAndWait()

            input("\nPress Enter to continue...")
            break

        case _:
            os.system('cls')
            print("Please input correct menu")

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty("voice", voices[1].id)

            # Say the text out loud
            engine.say("Please input correct menu")
            engine.runAndWait()

            input("\nPress Enter to continue...")
            os.system('cls')