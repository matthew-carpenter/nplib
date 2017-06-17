#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtts
import pygame

AUDIOPATH = '/audio/'

GREETING_ADAM = "Hi Adam, welcome to Matthew's apartment. Grab a beer and have a seat."
GREETING_JACI = "Hello Jacky, welcome to Matthew's apartment. You look nice today. Have a seat."

tts0 = gtts.gTTS(text=GREETING_ADAM, lang='en', slow=False)
tts0.save('/audio/greeting_adam.mp3')

tts1 = gtts.gTTS(text=GREETING_JACI, lang='en', slow=False)
tts1.save('/audio/greeting_jaci.mp3')

pygame.mixer.init()
pygame.mixer.music.load("greeting_adam.mp3")
pygame.mixer.music.play()

text = raw_input("Press any key to exit.")
