import datetime
import pygame
import webbrowser
import speech_recognition as sr
from gtts import gTTS

pygame.mixer.init()
pygame.mixer.music.load("./dexter sounds/1.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue


def main():
    def speak(text):
        tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def mic():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception:
                print("sorry couldn't recognize what you said!")

                pygame.mixer.init()
                pygame.mixer.music.load("./dexter sounds/2.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

                main()

        return said

    text = mic()

    if 'hello' in text or 'hey' in text:
        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/3.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        print("hey!")
        main()

    if 'hi' in text or "hai" in text:
        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/3.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        print("hey!")
        main()


    elif 'open Google' in text:
        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/4.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        webbrowser.get()
        webbrowser.open('https://www.google.com/')


    elif 'time' in text:
        toop = datetime.datetime.now().strftime('%H:%M')
        print(toop)

        speak(toop)

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/20.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()
    elif 'date' in text:
        toop = str(datetime.date.today())
        print(toop)

        speak(toop)

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/21.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'open Instagram' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/4.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        webbrowser.get()
        webbrowser.open('https://www.instagram.com/')

    elif 'open YouTube' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/4.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        webbrowser.get()
        webbrowser.open('https://www.youtube.com/')

    elif 'open Facebook' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/4.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        webbrowser.get()
        webbrowser.open('https://www.facebook.com/')

    elif 'your name' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/5.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("my name is Dexter")
        main()

    elif 'my name' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/6.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("Mitsu is your name")
        main()

    elif 'how are you' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/7.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("i am fine! what about you?")
        main()

    elif 'what are you doing' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/8.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("regretting my life choises")
        main()

    elif 'Dexter' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/9.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("yhea?")
        main()

    elif 'hay' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/10.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("whats up homie")
        main()

    elif 'who are you' in text or 'what are you' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/11.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("I am a program created my mr.mitsu-senpai")
        main()

    elif 'quit' in text or 'close' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/12.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        quit()

    elif 'exit' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/13.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        quit()

    elif 'I love you' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/14.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'how old are you' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/22.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()


    elif 'when were you created' in text or 'when were you born' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/23.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'when is your birthday' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/24.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'how old am I' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/25.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'when was I born' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/26.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'when is my birthday' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/27.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    elif 'who am I' in text:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/28.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        main()

    else:

        pygame.mixer.init()
        pygame.mixer.music.load("./dexter sounds/15.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

        print("want me to search in google?")

        thething = text

        def main2():

            def mic():

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    said = ""

                    try:
                        said = r.recognize_google(audio)
                        print(said)
                    except Exception:
                        print("sorry couldn't get that.")

                        pygame.mixer.init()
                        pygame.mixer.music.load("./dexter sounds/16.mp3")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy() == True:
                            continue

                        main2()

                return said

            text = mic()
            if 'yes' in text or 'yah' in text:
                print("searching...")

                pygame.mixer.init()
                pygame.mixer.music.load("./dexter sounds/17.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

                webbrowser.open(
                    "https://www.google.com/search?sxsrf=ALeKk00chtqsz3DmvQhgB_K1c8IItH9Yww%3A1590235124809&ei=9A_JXoKCMbHWz7sP_5K9-AQ&q=" + str(
                        thething) + "&oq=" + str(
                        thething) + "&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgvipoAHABeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiCzOS998npAhUx63MBHX9JD08Q4dUDCAw&uact=5")
                quit()


            elif 'yeah' in text:
                print("searching...")

                pygame.mixer.init()
                pygame.mixer.music.load("./dexter sounds/17.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

                webbrowser.open(
                    "https://www.google.com/search?sxsrf=ALeKk00chtqsz3DmvQhgB_K1c8IItH9Yww%3A1590235124809&ei=9A_JXoKCMbHWz7sP_5K9-AQ&q=" + str(
                        thething) + "&oq=" + str(
                        thething) + "&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgvipoAHABeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiCzOS998npAhUx63MBHX9JD08Q4dUDCAw&uact=5")
                quit()

            elif 'no' in text or 'nope' in text:

                pygame.mixer.init()
                pygame.mixer.music.load("./dexter sounds/18.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

                main()

            else:

                pygame.mixer.init()
                pygame.mixer.music.load("./dexter sounds/19.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

                print("dumbass, try again!")
                main2()

        main2()


main()