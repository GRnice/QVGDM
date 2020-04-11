import pygame
from Plateau import Plateau
from Partie import Partie
from Question_pack_1 import QuestionPack1
from QuestionPack2 import QuestionPack2
from QuestionPack3 import QuestionPack3
from QuestionPack4 import QuestionPack4
from random import randint
from SoundManager import SoundManager
from FileChooser import FileChooser
from Reader import Reader

class Main:
    def __init__(self):

        #questions = QuestionPack4().questions
        pygame.init()
        self.plateau = Plateau(1280, 700, "./images")
        self.partie = None
        self.sound_manager = SoundManager("./audio")

    # Call public -> P
    # Call friend -> J
    # 50/50       -> L
    # Reset       -> R
    # Next question -> N
    # A B C D -> SELECT RESPONSE
    # ENTER -> Show result
    # ESCAPE -> Quit game
    #

    def reset(self):
        filename = FileChooser().get_filename()
        questions = Reader(filename).get_questions()
        if questions is None:
            return False

        self.partie = Partie(questions)
        # reset game
        self.partie.reset()
        self.plateau.reset()
        self.sound_manager.reset()
        self.sound_manager.play_generic()
        return True


    def start_game(self):
        question = self.partie.get_current_question()
        index = self.partie.current_question_index

        self.sound_manager.start_party_jingle()
        self.plateau.fill_question_area(question)
        self.sound_manager.play_ongoing_question(index)

    def select_response(self, letter):
        question = self.partie.get_current_question()
        index = self.partie.current_question_index

        self.partie.select_response(letter)
        self.plateau.select_answer(question, letter)
        self.sound_manager.play_last_word(index)

    def show_response(self):
        question = self.partie.get_current_question()
        index = self.partie.current_question_index

        good = self.partie.response_is_good()
        if good:
            self.sound_manager.play_good_response(index)
            winned_price = self.partie.gains[index]
            self.plateau.good_response(question, winned_price, self.partie.letter_selected)

        else:
            self.sound_manager.play_wrong_answer()
            self.plateau.wrong_response(question, question.good_letter)

    def run(self):
        self.reset()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print("key")
                    print(event.key)
                    if event.key == pygame.K_q:
                        print("press A")
                        # answer a
                        self.select_response("A")

                    elif event.key == pygame.K_b:
                        print("press B")
                        # answer b
                        self.select_response("B")

                    elif event.key == pygame.K_c:
                        print("press C")
                        # answer c
                        self.select_response("C")

                    elif event.key == pygame.K_d:
                        print("press D")
                        # answer d
                        self.select_response("D")

                    elif event.key == pygame.K_p:
                        print("press P")
                        # public vote
                        # DISABLED

                    elif event.key == pygame.K_j:
                        print("press J")
                        # call friend
                        if self.partie.call_friend_available > 0:
                            self.partie.call_friend_available = self.partie.call_friend_available - 1
                            index = self.partie.current_question_index
                            self.sound_manager.play_call_friend(index)
                            if self.partie.call_friend_available == 0:
                                self.plateau.update_call_friend(False)
                    elif event.key == pygame.K_l:
                        print("press L")
                        # 50/50
                        if self.partie.fiftyfifty_available > 0:
                            self.partie.fiftyfifty_available = self.partie.fiftyfifty_available - 1
                            index = self.partie.current_question_index

                            question = self.partie.get_current_question()
                            choices = ["A", "B", "C", "D"]
                            choices.remove(question.good_letter)
                            first_answer_removed = choices[randint(0, len(choices) - 1)]
                            choices.remove(first_answer_removed)
                            second_answer_removed = choices[randint(0, len(choices) - 1)]

                            self.sound_manager.play_fifty_fifty()
                            self.plateau.hide_answers([first_answer_removed, second_answer_removed])
                            if self.partie.fiftyfifty_available == 0:
                                self.plateau.update_fifty_fifty(False)
                    elif event.key == pygame.K_r:
                        print("press R")
                        if self.reset():
                            pass
                        else:
                            self.running = False
                            pygame.quit()
                            return

                    elif event.key == pygame.K_s:
                        print("press S")
                        # start game
                        self.start_game()

                    elif event.key == pygame.K_n:
                        print("press N")
                        # next question
                        question = self.partie.next_question()
                        index = self.partie.current_question_index
                        self.plateau.fill_question_area(question)
                        self.sound_manager.play_ongoing_question(index)

                    elif event.key == pygame.K_RETURN:
                        print("press ENTER")
                        # enter show response
                        self.show_response()
                    elif event.key == pygame.K_ESCAPE:
                        print("press ESCAPE")
                        self.running = False
                        pygame.quit()
                        return

Main().run()