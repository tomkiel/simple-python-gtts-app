import os
import time
import webbrowser
from gtts import gTTS
import subprocess
from pynput.keyboard import Key, Controller
from utils import loader

app_configuration = {
    'world_name': 'Mutrix',
    'assistant_name': 'Lee'
}

user = os.environ['USERNAME']
devnull = open(os.devnull, 'w')


def user_fullname():
    """
    @return str
    Get user name from /etc/passwd
    """
    content = str(subprocess.run(["getent", "passwd", "{}".format(user)], stdout=subprocess.PIPE).stdout)
    content = content.split(":")
    return content[4] or user.capitalize


def welcome_message():
    """
    Initial app message
    """
    welcome_text = "Hello {}!\nYou're welcome to {} Reloaded! \n" \
                   "I'm {}, a virtual assistant created in Python!\n" \
                   "Please wait a few seconds!\n" \
                   "I'm setting up my basic systems.\n".format(user_fullname(),
                                                               app_configuration['world_name'],
                                                               app_configuration['assistant_name']
                                                               )

    print("\nConnect to internet!")
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-hide_banner", "assets/internet_90s.ogg"],
                    stdout=devnull, stderr=devnull)
    loader.loader_animation("Installing Internet Explorer 6...", 10)
    print("\nInternet is connected!\n\nLet's go!\nWhat's your name?\nWait! Your name is {}, right?".format(
        user_fullname()))
    speak_to_me("welcome_message_check_name",
                "Internet is connected!\nLet's go!\n"
                "What's your name?\nWait!"
                "Your name is {}, right?\n".format(user_fullname())
                )
    print("Ok, I'm ready!\n")
    speak_to_me("welcome_message_ready", "Ok, I'm ready!")
    print(welcome_text)
    speak_to_me("welcome_message", welcome_text)
    loader.loader_animation()


def speak_to_me(name, message):
    """
    Create audio file for message and play
    @params name: str
    @params message: str
    """
    speaker = gTTS(text=message, lang="en", slow=False)
    speaker.save("assets/" + name + ".mp3")
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-hide_banner", "assets/" + name + ".mp3"], stdout=devnull,
                    stderr=devnull)


def play_game():
    """
    Play a very simple game to guess the user's favorite song.
    """
    speak_to_me("like_music", "Do you like music?")
    like_music = input("Do you like music?y/n\n")
    if like_music == "y":
        print("Cool, {}!\n"
              "I like music a lot! \n"
              "My favorite song is He cheats on you from San Marino, and you? \n"
              "Wait, I'll try to guess!".format(user_fullname()))
        speak_to_me("like_music_yes", "Cool {}!\n,"
                                      "I like music a lot! \n"
                                      "My favorite song is He cheats on you from San Marino,\n"
                                      "and you? \n "
                                      "Wait, I'll try to guess!".format(user_fullname()))
        loader.loader_animation("Searching....", 5)
        time.sleep(2)
        try:
            webbrowser.get("google-chrome").open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        except webbrowser.Error:
            webbrowser.open("https://www.google.com/intl/pt-BR/chrome/")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif like_music == "n":
        print("Tell more about you...\nAre you living on Mars?\nI will suggest a really cool song!")
        speak_to_me(
            "like_music_no",
            "Tell more about you...\nAre you living on Mars?\nI will suggest a really cool song!")
        time.sleep(2)
        try:
            webbrowser.get("google-chrome").open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        except webbrowser.Error:
            webbrowser.open("https://www.google.com/intl/pt-BR/chrome/")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        print("Ok, no problem.\nTry again!\n")
        speak_to_me("error_play_game", "Ok, no problem. Try again!")
        play_game()


def start_new_game():
    """
    Interaction to start a new game with a simple approach to user interaction.

    """
    print("Let's start a game?\n")
    speak_to_me("welcome_message_start_game.mp3", "Let's start a game?\n")
    start_game = input("y/n\n")
    if start_game == "y":
        keyboard = Controller()
        keyboard.press(Key.f11)
        keyboard.release(Key.f11)
        play_game()
    elif start_game == "n":
        print("OK! I need to remove everything we did together!\nI'm sad... {}, you're a very bad people!".format(
            user_fullname()))
        speak_to_me("no_play_game",
                    "OK! I need to remove everything we did together!\nI'm sad... {}, you're a very bad people!".format(
                        user_fullname())
                    )
        loader.loader_animation("Running...", 10)
        print("Download Windows Vista to you!")
        loader.loader_animation("Downloading to /home/{}/Downloads".format(user))
        subprocess.run(["touch", "/home/{}/Downloads/WinVista.iso".format(user)], stdout=subprocess.PIPE)
        subprocess.run(
            ["dd", "if=/dev/zero", "of=/home/{}/Downloads/WinVista.iso".format(user), "bs=1024", "count=1048576"],
            stdout=subprocess.PIPE)
        print("Installing Baidu!\n")
        loader.loader_animation("Installing Baidu!", 20)
        print("Bye bye, see you on hell!")
        speak_to_me("bye_bye", "Bye bye, see you in hell, baby")
        webbrowser.open("https://github.com/tomkiel")
    else:
        print("Ok, no problem.\nTry again!\n")
        speak_to_me("error_play_game", "Ok, no problem. Try again!")
        start_new_game()


def main():
    """
    It is a very simple application that uses gTTS, interacts with the shell, plays music and runs software
    @Regis Tomkiel
    """
    subprocess.call("clear")
    welcome_message()
    start_new_game()


if __name__ == '__main__':
    main()
