#RoboSpeaker🤖
"""
Hey there this is my next mini project which is a robo speaker this speaker pronunces out
the text we give in as input.This can be implemented in training robots etc.As of now I
have programmed this in such a way that it works on mac,linux and windows.This code only
executes directly as I have given the condition __name__=='__main__'.
---19-12-2025
"""

import os
import platform

def speak(text):
    system = platform.system()

    if system == "Darwin":          
        os.system(f"say '{text}'")

    elif system == "Linux":         
        os.system(f"espeak '{text}'")

    elif system == "Windows":       
        os.system(
            f'powershell -Command "Add-Type -AssemblyName System.Speech; '
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
        )

    else:
        print("Text-to-speech not supported on this OS")

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1 Created by Prathul P")

    while True:
        x = input("Enter what do you want me to pronounce (q to quit): ")

        if x == "q":
            speak("bye bye friend")
            break

        speak(x)
