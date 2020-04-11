import pygame
import time

class SoundManager:
    def __init__(self, sound_path):
        self.sound_path = sound_path
        # initialize pygame.mixer
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2 ** 12)
        # init() channels refers to mono vs stereo, not playback Channel object

        # create separate Channel objects for simultaneous playback
        self.mainTheme = pygame.mixer.Channel(0)  # argument must be int
        self.effects = pygame.mixer.Channel(1)  # argument must be int
        self.load()

    def load(self):
        self.generic_sound = pygame.mixer.Sound((self.sound_path + '/Generic_QVGDM.wav').encode())
        self.ending_game = pygame.mixer.Sound((self.sound_path + '/Ending_game_QVGDM.wav').encode())
        self.start_party_sound = pygame.mixer.Sound((self.sound_path + '/Start_question_for_200_QVGDM.wav').encode())

        # wrong
        self.wrong_answer_sound = pygame.mixer.Sound((self.sound_path + '/losing/Wrong_answer_QVGDM.wav').encode())

        # Winning
        self.good_answer_200_to_800_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_200_to_800_QVGDM.wav').encode())

        self.good_answer_1500_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_1500_QVGDM.wav').encode())

        self.good_answer_3000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_3000_QVGDM.wav').encode())

        self.good_answer_6000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_6000_QFGDM.wav').encode())

        self.good_answer_12000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_12K_QVGDM.wav').encode())

        self.good_answer_24000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_24K_QVGDM.wav').encode())

        self.good_answer_48000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_48K_QVGDM.wav').encode())

        self.good_answer_72000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_72K_QVGDM.wav').encode())

        self.good_answer_100000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_100K_QVGDM.wav').encode())

        self.good_answer_150000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_150K_QVGDM.wav').encode())

        self.good_answer_300000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_300K_QVGDM.wav').encode())

        self.good_answer_1000000_sound = pygame.mixer.\
            Sound((self.sound_path + '/winning/Win_for_1M_QVGDM.wav').encode())

        # ongoing question
        self.ongoing_question_for_200_to_1500_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_200_to_1500_QVGDM.wav').encode())

        self.ongoing_question_for_3000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_3K_QVGDM.wav').encode())

        self.ongoing_question_for_6000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_6K_QVGDM.wav').encode())

        self.ongoing_question_for_12000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_12K_QVGDM.wav').encode())

        self.ongoing_question_for_24000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_24K_QVGDM.wav').encode())

        self.ongoing_question_for_48000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_48K_QVGDM.wav').encode())

        self.ongoing_question_for_72000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_72K_QVGDM.wav').encode())

        self.ongoing_question_for_100000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_100K_QVGDM.wav').encode())

        self.ongoing_question_for_150000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_150K_QVGDM.wav').encode())

        self.ongoing_question_for_300000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_300K_QVGDM.wav').encode())

        self.ongoing_question_for_1000000_sound = pygame.mixer.\
            Sound((self.sound_path + '/ongoing_questions/Question_for_1M_QVGDM.wav').encode())

        # Last word
        self.last_word_for_3000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_3K_QVGDM.wav').encode())

        self.last_word_for_6000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_6K_QVGDM.wav').encode())

        self.last_word_for_12000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_12K_QVGDM.wav').encode())

        self.last_word_for_24000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_24K_QVGDM.wav').encode())

        self.last_word_for_48000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_48K_QVGDM.wav').encode())

        self.last_word_for_72000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_72K_QVGDM.wav').encode())

        self.last_word_for_100000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_100K_QVGDM.wav').encode())

        self.last_word_for_150000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_150K_QVGDM.wav').encode())

        self.last_word_for_300000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_300K_QVGDM.wav').encode())

        self.last_word_for_1000000_sound = pygame.mixer.\
            Sound((self.sound_path + '/last_word/Last_word_for_1M_QVGDM.wav').encode())

        #Joker
        self.call_friend_sound = pygame.mixer.Sound((self.sound_path + '/jokers/Call_friend_ongoing_QVGDM.wav').encode())
        self.fifty_fifty_effect_sound = pygame.mixer.Sound((self.sound_path + '/jokers/50_50_effect_QVGDM.wav').encode())

    def start_party_jingle(self):
        self.mainTheme.stop()
        self.mainTheme.play(self.start_party_sound, maxtime=7000)
        while self.mainTheme.get_busy() > 0:
            time.sleep(1)

        return True

    def play_generic(self):
        self.mainTheme.stop()
        self.mainTheme.play(self.generic_sound)

    def reset(self):
        self.mainTheme.stop()
        self.effects.stop()

    def play_wrong_answer(self):
        self.mainTheme.stop()
        self.mainTheme.play(self.wrong_answer_sound)

    def play_fifty_fifty(self):
        self.effects.stop()
        self.effects.play(self.fifty_fifty_effect_sound)

    def play_call_friend(self, question_index):
        print("play_call_friend")
        self.mainTheme.stop()
        self.mainTheme.play(self.call_friend_sound)
        while self.mainTheme.get_busy() > 0:
            time.sleep(1)

        self.play_ongoing_question(question_index)

    def play_ongoing_question(self, question_index):

        if question_index == 0:
            # 200
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_200_to_1500_sound, loops=-1)
        elif question_index == 1:
            # 300
            pass
        elif question_index == 2:
            # 500
            pass
        elif question_index == 3:
            # 800
            pass
        elif question_index == 4:
            # 1.5K
            pass
        elif question_index == 5:
            # 3K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_3000_sound, loops=-1)
        elif question_index == 6:
            # 6K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_6000_sound, loops=-1)
        elif question_index == 7:
            # 12K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_12000_sound, loops=-1)
        elif question_index == 8:
            # 24K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_24000_sound, loops=-1)
        elif question_index == 9:
            # 48K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_48000_sound, loops=-1)
        elif question_index == 10:
            # 72K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_72000_sound, loops=-1)
        elif question_index == 11:
            # 100K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_100000_sound, loops=-1)
        elif question_index == 12:
            # 150K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_150000_sound, loops=-1)
        elif question_index == 13:
            # 300K
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_300000_sound, loops=-1)
        elif question_index == 14:
            # 1M
            self.mainTheme.stop()
            self.mainTheme.play(self.ongoing_question_for_1000000_sound, loops=-1)


    def play_last_word(self, question_index):

        if question_index == 0:
            # 200
            pass
        elif question_index == 1:
            # 300
            pass
        elif question_index == 2:
            # 500
            pass
        elif question_index == 3:
            # 800
            pass
        elif question_index == 4:
            # 1.5K
            pass
        elif question_index == 5:
            # 3K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_3000_sound)
        elif question_index == 6:
            # 6K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_6000_sound)
        elif question_index == 7:
            # 12K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_12000_sound)
        elif question_index == 8:
            # 24K
            self.mainTheme.play(self.last_word_for_24000_sound)
        elif question_index == 9:
            # 48K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_48000_sound)
        elif question_index == 10:
            # 72K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_72000_sound)
        elif question_index == 11:
            # 100K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_100000_sound)
        elif question_index == 12:
            # 150K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_150000_sound)
        elif question_index == 13:
            # 300K
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_300000_sound)
        elif question_index == 14:
            # 1M
            self.mainTheme.stop()
            self.mainTheme.play(self.last_word_for_1000000_sound)

    def play_good_response(self, question_index):
        if question_index == 0:
            # 200
            self.effects.stop()
            self.effects.play(self.good_answer_200_to_800_sound)
        elif question_index == 1:
            # 300
            self.effects.stop()
            self.effects.play(self.good_answer_200_to_800_sound)
        elif question_index == 2:
            # 500
            self.effects.stop()
            self.effects.play(self.good_answer_200_to_800_sound)
        elif question_index == 3:
            # 800
            self.effects.stop()
            self.effects.play(self.good_answer_200_to_800_sound)
        elif question_index == 4:
            # 1.5K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_1500_sound)
        elif question_index == 5:
            # 3K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_3000_sound)
        elif question_index == 6:
            # 6K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_6000_sound)
        elif question_index == 7:
            # 12K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_12000_sound)
        elif question_index == 8:
            # 24K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_24000_sound)
        elif question_index == 9:
            # 48K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_48000_sound)
        elif question_index == 10:
            # 72K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_72000_sound)
        elif question_index == 11:
            # 100K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_100000_sound)
        elif question_index == 12:
            # 150K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_150000_sound)
        elif question_index == 13:
            # 300K
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_300000_sound)
        elif question_index == 14:
            # 1M
            self.mainTheme.stop()
            self.mainTheme.play(self.good_answer_1000000_sound)