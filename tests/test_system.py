import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from model.qa_engine import get_answer
from model.qa_engine import get_answer


questions = [

    "What is artificial intelligence?",

    "Explain machine learning",

    "What is nsuo?",

    "Translate water into Twi",

    "What is Python programming?",

    "Tell me about Ghana"

]


# Retained as a manual demo script.  It must not issue live requests merely
# because a test runner imports this module during discovery.
if __name__ != "__main__":
    questions = []


for question in questions:

    print("\n==============================")
    print("QUESTION:")
    print(question)


    answer, source = get_answer(question)


    print("\nSOURCE:")
    print(source)


    print("\nANSWER:")
    print(answer)
