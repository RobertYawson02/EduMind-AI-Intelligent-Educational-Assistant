from model.query_engine import create_query_plan

questions = [
    "What is the meaning of nsuo?",
    "What does nsuo retɔ mean?",
    "How do you say I am hungry in Twi?",
    "What is the meaning of ɔdɔ?",
    "Translate water into Twi",
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)

    plan = create_query_plan(question)

    print("LANGUAGE:", plan["language"])
    print("AKAN:", plan["is_akan"])
    print("TYPE:", plan["query_type"])
    print("TOPIC:", plan["topic"])
    print("TARGET:", plan["target"])

    print("\nQUERIES:")

    for i, query in enumerate(plan["queries"], 1):
        print(f"{i}. {query}")