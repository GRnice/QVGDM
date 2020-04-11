import pygame
import time

WIDTH = 1280
HEIGHT = 700

QUESTION_AREA_WIDTH = WIDTH
QUESTION_AREA_HEIGHT = HEIGHT * 0.4

PURPLE_COLOR = [103, 125, 181]
GREEN_COLOR = [15, 219, 96]
ORANGE_COLOR = [237, 178, 74]

WHITE_TEXT_COLOR = (255, 255, 255)
BLACK_TEXT_COLOR = (0, 0, 0)

PI = 3.1415

class Plateau:
    def __init__(self, width, height, path_image):
        self.width = width
        self.height = height
        self.path_image = path_image
        self.reset()

    def reset(self):
        self.screen = pygame.display.set_mode((1280, 700))
        self.font_question = pygame.font.SysFont("calibri", 40)
        self.font_answer = pygame.font.SysFont("calibri", 30)

        self.fifty_fifty_available_image = pygame.image.load((self.path_image + '/fifty_fifty_available_QVGDM.jpg').encode())
        self.fifty_fifty_expired_image = pygame.image.load((self.path_image + '/fifty_fifty_expired_QVGDM.jpg').encode())

        self.call_friend_available_image = pygame.image.load((self.path_image + '/call_friend_available_QVGDM.jpg').encode())
        self.call_friend_expired_image = pygame.image.load((self.path_image + '/call_friend_expired_QVGDM.jpg').encode())

        black = [0, 0, 0]
        self.screen.fill(black)
        pygame.display.flip()

        self.update_fifty_fifty(True)
        self.update_call_friend(True)

        # left, top, width, height
        rectangle_questions_area_coords = [0, QUESTION_AREA_HEIGHT, WIDTH, HEIGHT - QUESTION_AREA_HEIGHT]

        self.rectangle_question_area_coords = [10, QUESTION_AREA_HEIGHT + 20, WIDTH - 20, 120]
        self.rectangle_answer_a_area_coords = [10, QUESTION_AREA_HEIGHT + 150, 640, 100]
        self.rectangle_answer_b_area_coords = [660, QUESTION_AREA_HEIGHT + 150, WIDTH - 665, 100]
        self.rectangle_answer_c_area_coords = [10, QUESTION_AREA_HEIGHT + 260, 640, 100]
        self.rectangle_answer_d_area_coords = [660, QUESTION_AREA_HEIGHT + 260, WIDTH - 665, 100]

        # draw rectangle questions AREA
        pygame.draw.rect(self.screen, [0, 0, 0], rectangle_questions_area_coords, 2)

        # draw question area
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_question_area_coords, 6)

        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_answer_a_area_coords, 3)
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_answer_b_area_coords, 3)
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_answer_c_area_coords, 3)
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_answer_d_area_coords, 3)
        pygame.display.flip()

    def fill_purple(self, rectangle):
        pygame.draw.rect(self.screen, PURPLE_COLOR, rectangle)

    def fill_green(self, rectangle):
        pygame.draw.rect(self.screen, GREEN_COLOR, rectangle)

    def fill_orange(self, rectangle):
        pygame.draw.rect(self.screen, ORANGE_COLOR, rectangle)

    def fill_question_area(self, question):

        self.fill_purple(self.rectangle_answer_a_area_coords)
        self.fill_purple(self.rectangle_answer_b_area_coords)
        self.fill_purple(self.rectangle_answer_c_area_coords)
        self.fill_purple(self.rectangle_answer_d_area_coords)

        self.show_question(question.question)
        self.show_response_a(question.response_a_str, WHITE_TEXT_COLOR)
        self.show_response_b(question.response_b_str, WHITE_TEXT_COLOR)
        self.show_response_c(question.response_c_str, WHITE_TEXT_COLOR)
        self.show_response_d(question.response_d_str, WHITE_TEXT_COLOR)
        pygame.display.flip()

    def hide_answers(self, answers):
        for answer in answers:
            if answer == "A":
                self.fill_purple(self.rectangle_answer_a_area_coords)
            elif answer == "B":
                self.fill_purple(self.rectangle_answer_b_area_coords)
            elif answer == "C":
                self.fill_purple(self.rectangle_answer_c_area_coords)
            elif answer == "D":
                self.fill_purple(self.rectangle_answer_d_area_coords)

    def update_fifty_fifty(self, available):
        print("update_fifty_fifty()")
        if available:
            print("update_fifty_fifty(True)")
            self.screen.blit(self.fifty_fifty_available_image, (1100, 20))
        else:
            print("update_fifty_fifty(False)")
            self.screen.blit(self.fifty_fifty_expired_image, (1100, 20))
        pygame.display.flip()

    def update_call_friend(self, available):
        if available:
            print("update_call_friend(True)")
            self.screen.blit(self.call_friend_available_image, (950, 20))
        else:
            print("update_call_friend(False)")
            self.screen.blit(self.call_friend_expired_image, (950, 20))

        pygame.display.flip()

    def show_gain(self, gain):
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_question_area_coords, 6)
        pygame.draw.rect(self.screen, [0, 0, 0], [16, QUESTION_AREA_HEIGHT + 26, WIDTH - 26, 114])
        text = self.font_question.render(str(gain), True, WHITE_TEXT_COLOR)
        self.screen.blit(text, (WIDTH // 2, QUESTION_AREA_HEIGHT + 60))

    def show_question(self, question):
        pygame.draw.rect(self.screen, PURPLE_COLOR, self.rectangle_question_area_coords, 6)
        pygame.draw.rect(self.screen, [0, 0, 0], [16, QUESTION_AREA_HEIGHT + 26, WIDTH - 26, 114])
        if len(question) > 75:
            text1 = self.font_question.render(str(question[0:71] + '-'), True, WHITE_TEXT_COLOR)
            text2 = self.font_question.render(str(question[71:]), True, WHITE_TEXT_COLOR)
            self.screen.blit(text1, (30, QUESTION_AREA_HEIGHT + 30))
            self.screen.blit(text2, (30, QUESTION_AREA_HEIGHT + 60))
        else:
            text = self.font_question.render(str(question), True, WHITE_TEXT_COLOR)
            self.screen.blit(text, (20, QUESTION_AREA_HEIGHT + 30))

    def show_response_a(self, text, color):
        if len(text) > 45:
            text1 = text[0:45] + '-'
            text2 = text[45:]
            rendered_answer_a_part_1 = self.font_answer.render(str(text1), True, color)
            rendered_answer_a_part_2 = self.font_answer.render(str(text2), True, color)
            self.screen.blit(rendered_answer_a_part_1, (50, QUESTION_AREA_HEIGHT + 165))
            self.screen.blit(rendered_answer_a_part_2, (50, QUESTION_AREA_HEIGHT + 200))
        else:
            rendered_answer_a = self.font_answer.render(str(text), True, color)
            self.screen.blit(rendered_answer_a, (50, QUESTION_AREA_HEIGHT + 165))

    def show_response_b(self, text, color):
        if len(text) > 45:
            text1 = text[0:45] + '-'
            text2 = text[45:]
            rendered_answer_b_part_1 = self.font_answer.render(str(text1), True, color)
            rendered_answer_b_part_2 = self.font_answer.render(str(text2), True, color)
            self.screen.blit(rendered_answer_b_part_1, (700, QUESTION_AREA_HEIGHT + 165))
            self.screen.blit(rendered_answer_b_part_2, (700, QUESTION_AREA_HEIGHT + 200))
        else:
            rendered_answer_b = self.font_answer.render(str(text), True, color)
            self.screen.blit(rendered_answer_b, (700, QUESTION_AREA_HEIGHT + 165))

    def show_response_c(self, text, color):
        if len(text) > 45:
            text1 = text[0:45] + '-'
            text2 = text[45:]
            rendered_answer_c_part_1 = self.font_answer.render(str(text1), True, color)
            rendered_answer_c_part_2 = self.font_answer.render(str(text2), True, color)
            self.screen.blit(rendered_answer_c_part_1, (50, QUESTION_AREA_HEIGHT + 275))
            self.screen.blit(rendered_answer_c_part_2, (50, QUESTION_AREA_HEIGHT + 310))
        else:
            rendered_answer_c = self.font_answer.render(str(text), True, color)
            self.screen.blit(rendered_answer_c, (50, QUESTION_AREA_HEIGHT + 275))

    def show_response_d(self, text, color):
        if len(text) > 45:
            text1 = text[0:45] + '-'
            text2 = text[45:]
            rendered_answer_d_part_1 = self.font_answer.render(str(text1), True, color)
            rendered_answer_d_part_2 = self.font_answer.render(str(text2), True, color)
            self.screen.blit(rendered_answer_d_part_1, (700, QUESTION_AREA_HEIGHT + 275))
            self.screen.blit(rendered_answer_d_part_2, (700, QUESTION_AREA_HEIGHT + 310))
        else:
            rendered_answer_d = self.font_answer.render(str(text), True, color)
            self.screen.blit(rendered_answer_d, (700, QUESTION_AREA_HEIGHT + 275))

    def good_response(self, question, winned_price, letter):
        iteration_animation = 7
        self.show_gain(winned_price)
        while iteration_animation > 0:
            if letter == "A":
                self.fill_purple(self.rectangle_answer_a_area_coords)
                self.show_response_a(question.response_a_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_a_area_coords)
                self.show_response_a(question.response_a_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif letter == "B":
                self.fill_purple(self.rectangle_answer_b_area_coords)
                self.show_response_b(question.response_b_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_b_area_coords)
                self.show_response_b(question.response_b_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif letter == "C":
                self.fill_purple(self.rectangle_answer_c_area_coords)
                self.show_response_c(question.response_c_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_c_area_coords)
                self.show_response_c(question.response_c_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif letter == "D":
                self.fill_purple(self.rectangle_answer_d_area_coords)
                self.show_response_d(question.response_d_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_d_area_coords)
                self.show_response_d(question.response_d_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            time.sleep(0.2)
            iteration_animation = iteration_animation - 1

        pygame.display.flip()

    def wrong_response(self, question, rightLetter):
        iteration_animation = 7
        while iteration_animation > 0:
            if rightLetter == "A":
                self.fill_purple(self.rectangle_answer_a_area_coords)
                self.show_response_a(question.response_a_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_a_area_coords)
                self.show_response_a(question.response_a_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif rightLetter == "B":
                self.fill_purple(self.rectangle_answer_b_area_coords)
                self.show_response_b(question.response_b_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_b_area_coords)
                self.show_response_b(question.response_b_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif rightLetter == "C":
                self.fill_purple(self.rectangle_answer_c_area_coords)
                self.show_response_c(question.response_c_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_c_area_coords)
                self.show_response_c(question.response_c_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            elif rightLetter == "D":
                self.fill_purple(self.rectangle_answer_d_area_coords)
                self.show_response_d(question.response_d_str, BLACK_TEXT_COLOR)
                pygame.display.flip()
                time.sleep(0.2)
                self.fill_green(self.rectangle_answer_d_area_coords)
                self.show_response_d(question.response_d_str, WHITE_TEXT_COLOR)
                pygame.display.flip()
            time.sleep(0.2)
            iteration_animation = iteration_animation - 1

        pygame.display.flip()

    def select_answer(self, question, letter):
        if letter == "A":
            self.fill_orange(self.rectangle_answer_a_area_coords)
            self.show_response_a(question.response_a_str, BLACK_TEXT_COLOR)
        elif letter == "B":
            self.fill_orange(self.rectangle_answer_b_area_coords)
            self.show_response_b(question.response_b_str, BLACK_TEXT_COLOR)
        elif letter == "C":
            self.fill_orange(self.rectangle_answer_c_area_coords)
            self.show_response_c(question.response_c_str, BLACK_TEXT_COLOR)
        elif letter == "D":
            self.fill_orange(self.rectangle_answer_d_area_coords)
            self.show_response_d(question.response_d_str, BLACK_TEXT_COLOR)

        pygame.display.flip()