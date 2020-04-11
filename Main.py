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

filename = FileChooser().get_filename()
questions = Reader(filename).get_questions()

#questions = QuestionPack4().questions
pygame.init()
plateau = Plateau(1280, 700, "./images")
print(questions)
partie = Partie(questions)
sound_manager = SoundManager("./audio")

# Call public -> P
# Call friend -> M
# 50/50       -> L
# Reset       -> R
# Next question -> N
# A B C D -> SELECT RESPONSE
# ENTER -> Show result
#
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("key")
            print(event.key)
            if event.key == pygame.K_q:
                print("press A")
                # answer a
                question = partie.get_current_question()
                index = partie.current_question_index

                partie.select_response("A")
                plateau.select_answer(question, "A")
                sound_manager.play_last_word(index)

            elif event.key == pygame.K_b:
                print("press B")
                # answer b
                question = partie.get_current_question()
                index = partie.current_question_index

                partie.select_response("B")
                plateau.select_answer(question, "B")
                sound_manager.play_last_word(index)

            elif event.key == pygame.K_c:
                print("press C")
                # answer c
                question = partie.get_current_question()
                index = partie.current_question_index

                partie.select_response("C")
                plateau.select_answer(question, "C")
                sound_manager.play_last_word(index)

            elif event.key == pygame.K_d:
                print("press D")
                # answer d
                question = partie.get_current_question()
                index = partie.current_question_index

                partie.select_response("D")
                plateau.select_answer(question, "D")
                sound_manager.play_last_word(index)

            elif event.key == pygame.K_p:
                print("press P")
                # public vote
                if partie.vote_public_available:
                    partie.vote_public_available = False

            elif event.key == pygame.K_m:
                print("press M")
                # call friend
                if partie.call_friend_available > 0:
                    partie.call_friend_available = partie.call_friend_available - 1
                    print(partie.call_friend_available)
                    index = partie.current_question_index
                    sound_manager.play_call_friend(index)
                    if partie.call_friend_available == 0:
                        plateau.update_call_friend(False)
            elif event.key == pygame.K_l:
                print("press L")
                # 50/50
                if partie.fiftyfifty_available > 0:
                    partie.fiftyfifty_available = partie.fiftyfifty_available - 1
                    index = partie.current_question_index

                    question = partie.get_current_question()
                    choices = ["A", "B", "C", "D"]
                    choices.remove(question.good_letter)
                    first_answer_removed = choices[randint(0, len(choices) - 1)]
                    choices.remove(first_answer_removed)
                    second_answer_removed = choices[randint(0, len(choices) - 1)]

                    sound_manager.play_fifty_fifty()
                    plateau.hide_answers([first_answer_removed, second_answer_removed])
                    if partie.fiftyfifty_available == 0:
                        plateau.update_fifty_fifty(False)
            elif event.key == pygame.K_r:
                print("press R")
                # reset game
                partie.reset()
                plateau.reset()
                sound_manager.reset()
                sound_manager.play_generic()

            elif event.key == pygame.K_s:
                print("press S")
                # start game
                question = partie.get_current_question()
                index = partie.current_question_index

                res = sound_manager.start_party_jingle()
                plateau.fill_question_area(question)
                sound_manager.play_ongoing_question(index)

            elif event.key == pygame.K_n:
                print("press N")
                # next question
                question = partie.next_question()
                index = partie.current_question_index
                plateau.fill_question_area(question)
                sound_manager.play_ongoing_question(index)

            elif event.key == pygame.K_RETURN:
                print("press ENTER")
                # enter show response
                question = partie.get_current_question()
                index = partie.current_question_index

                good = partie.response_is_good()
                if good:
                    sound_manager.play_good_response(index)
                    winned_price = partie.gains[index]
                    plateau.good_response(question, winned_price, partie.letter_selected)

                else:
                    sound_manager.play_wrong_answer()
                    plateau.wrong_response(question, question.good_letter)

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
