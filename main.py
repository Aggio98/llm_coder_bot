import os
from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL_GPT, MODEL_LLAMA, SYSTEM_PROMPT


load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
ollama_api_key = os.getenv('OLLAMA_API_KEY')
ollama_base_url = os.getenv('OLLAMA_BASE_URL')

openai = OpenAI()
ollama = OpenAI(base_url=ollama_base_url, api_key=ollama_api_key)


def ask_gpt(question):
    stream = openai.chat.completions.create(
        model=MODEL_GPT,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        stream=True
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)

def ask_llama(question):
    stream = ollama.chat.completions.create(
        model=MODEL_LLAMA,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        stream=True
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)

def gpt_choice():
    while True:
        print("\n\nWhat is your coding question?")
        question = input("\nQuestion: ")

        if question.lower() == "quit":
            exit()
        if question.lower() == "back":
            return
        ask_gpt(question)



def llama_choice():
    while True:
        print("\n\nWhat is your coding question?")
        question = input("\nQuestion: ")

        if question.lower() == "quit":
            exit()
        if question.lower() == "back":
            return
        ask_llama(question)

def show_help():
    print("""
Commands:
    - help  List of commands
    - back  Use this command to go back after choosing a model
    - quit  Exits the chat
""")

def main():
    print('\nWelcome to the Coding Expert\n\nType "help" to get a list of commands')
    while True:
        cmd = input("\nPick a large language model to use:\n\n1. OpenAI\n2. Ollama\n\nModel: ")
        match cmd:
            case "1":
                gpt_choice()
            case "2":
                llama_choice()
            case "help":
                show_help()
            case "quit":
                break
            case _:
                print("\nInvalid option")

if __name__ == "__main__":
    main()