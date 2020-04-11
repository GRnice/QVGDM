import json
from Partie import Question

class Reader:
    def __init__(self, filename):
        self.filename = filename

    def get_questions(self):
        try:
            with open(self.filename) as f:
                questions = []
                data = json.load(f)["questions"]
                if len(data) != 15:
                    return None
                for question_raw in data:
                    print("question_raw ", question_raw)
                    for key, raw in question_raw.items():
                        print("raw:", raw)
                        questions.append(Question(raw["QUESTION"], raw["REPONSE_A"],
                                                  raw["REPONSE_B"], raw["REPONSE_C"],
                                                  raw["REPONSE_D"], raw["REPONSE"]))

                return questions
        except Exception as err:
            print("??", err)
            return None
