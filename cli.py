import os
from retriever import generate_answer

def interactive_qa():
    print("Interactive CLI. Type 'exit' to quit.")
    print("Use command ':mode local', ':mode model' to change answering mode.\n")

    answer_mode = os.getenv("DEFAULT_ANSWER_MODE", "local")

    while True:
        q = input("Your question: ").strip()
        if q.lower() == "exit":
            break
        if q.startswith(":mode "):
            mode = q.split(":mode", 1)[1].strip()
            if mode in ["local", "model"]:
                answer_mode = mode
                print(f"Answer mode set to '{answer_mode}'\n")
            else:
                print("Invalid mode. Choose from: local, model\n")
            continue

        print(f"Answer (mode={answer_mode}): {generate_answer(q, answer_mode)}\n")
