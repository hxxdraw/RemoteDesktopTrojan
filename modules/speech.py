"""
Sound player
"""


from pygame.mixer import init, music
from pyttsx3 import init as speech_init


class Speech(object):
    def __init__(self, rate, index, volume, text):
        """
        :param rate:
        :param index:
        :param volume:
        :param text:
        """
        self.speech_rate = rate
        self.voice_index = index
        self.sound_volume = volume
        self.phrase = text

    def Synthesize(self):
        """
        Generating  speech using voice_id/volume/rate
        :return: None
        """
        engine = speech_init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.voice_index].id)
        engine.setProperty('rate', self.speech_rate)
        engine.setProperty('volume', self.sound_volume)
        engine.say(self.phrase)
        engine.runAndWait()
        engine.stop()


class Sound(object):
    def __init__(self):
        """
        initiating sound module
        """
        init()

    @staticmethod
    def Play(file_path):
        """
        Playing sound using <self.path> ;== file_path
        :return:
        """
        music.load(file_path)   # loading sound
        music.play()    # plating sound
