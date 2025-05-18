import json
BASE_DIR = "C:/Users/elvin/PycharmProjects/Gen-AI-and-Agentic-AI-class/"
def read_user():
    with open(f"{BASE_DIR}data/users.json") as stream:
        users = json.load(stream)
        return users


def read_questions(position: int):
    with open(f"{BASE_DIR}data/questions.json") as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            res = question.get('question')
            print(res)
            return res

def read_alternatives(q_id:int):
    with open(f"{BASE_DIR}data/alternatives.json") as alternatives:
        alternate=json.load(alternatives)

    for options in alternate:
        if options['question_id']==q_id:
            # print(options.get('alternative'))
            return options.get('alternative')



if __name__ == "__main__":
    # print(read_user())
    # read_questions(1)
    print(read_alternatives(2))





