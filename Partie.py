
class Question:
    def __init__(self, question_str, response_a_str, response_b_str,
                 response_c_str, response_d_str, good_letter):
        """

        :param question_str:
        :param response_a_str:
        :param response_b_str:
        :param response_c_str:
        :param response_d_str:
        :param good_response_index:
        """
        
        self.question = question_str
        self.response_a_str = response_a_str
        self.response_b_str = response_b_str
        self.response_c_str = response_c_str
        self.response_d_str = response_d_str
        self.good_letter = good_letter

    def is_good_response(self, letter_selected):
        return self.good_letter == letter_selected


class Partie:
    def __init__(self, questions_array):
        self.questions_array = questions_array
        self.letter_selected = ""
        self.fiftyfifty_available = 1
        self.call_friend_available = 2
        self.vote_public_available = 1
        self.current_question_index = 0

        self.gains = ["200€", "300€", "500€", "800€", "1500€",
                      "3000€", "6000€", "12000€", "24000€" , "48000€",
                      "72000€", "100000€" , "150000€" , "300000€",
                      "1000000€"]
        self.paliers = [0, 1500, 48000]

        self.reset()

    def reset(self):
        self.fiftyfifty_available = 1
        self.call_friend_available = 2
        self.vote_public_available = 1
        self.current_question_index = 0
        self.letter_selected = ""

    def next_question(self):
        self.current_question_index = self.current_question_index + 1
        self.letter_selected = ""
        return self.questions_array[self.current_question_index]

    def get_current_question(self):
        return self.questions_array[self.current_question_index]

    def select_response(self, letter_selected):
        self.letter_selected = letter_selected

    def response_is_good(self):
        if self.letter_selected == "":
            return None
        else:
            question = self.questions_array[self.current_question_index]
            return question.is_good_response(self.letter_selected)