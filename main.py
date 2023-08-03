# Author: Sethispr, Date: 28 July 2023
# fixed code so it will directly install requirements.
# will add progress bar and remove loading animation and price of tokens used in USD/CAD.

import os
import openai
import sys
import time
import subprocess
from colorama import Back, Fore, Style

def install_requirements():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.yml"])
    except Exception as e:
        print(f"Error occurred while installing requirements: {e}")
        exit(1)

def loading_animation(duration):
    animation = "|/-\\"
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        for char in animation:
            sys.stdout.write(f"\rLoading {char}")
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write("\rLoading..\n")
    sys.stdout.flush()

def save_to_file(text):
    while True:
        filename = input("Enter the filename to save (excluding '.py' extension and not 'main'): ")
        if filename == "main":
            print("You cannot save to 'main.py'. Please choose a different filename.")
        else:
            filename_with_extension = f"{filename}.py"
            if os.path.exists(filename_with_extension):
                print(f"A file with the name '{filename_with_extension}' already exists.\nPlease choose a different filename.")
            else:
                with open(filename_with_extension, "w") as file:
                    file.write(text)
                print(f"Code saved to '{filename_with_extension}' successfully!\nDon't see the file? Press 'Show Code' and tap '{filename_with_extension}' to copy the code")
                break

def create_code_with_prompt(prompt, max_tokens):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.6
    )
    return response['choices'][0]['text'], response['usage']['total_tokens']

def main():
    install_requirements()

    print(Back.CYAN+'                            '+Back.RESET+' (Tip: View console in full-screen for better appearance.)')
    api_key = input(Style.BRIGHT + Back.BLACK + "Insert" + Style.BRIGHT + Back.BLACK + Fore.CYAN + " OpenAI" + Style.BRIGHT + Back.BLACK + Fore.WHITE + " API key: -->  ")
    openai.api_key = api_key

    coding_language = input(Style.BRIGHT + Back.RESET + "Which" + Style.BRIGHT + Fore.CYAN + Back.BLACK + " coding language" + Style.BRIGHT + Back.RESET + Fore.RESET + " would you like? -->  ")
    initial_input = input("Insert a"+Back.BLACK+Fore.CYAN+" Code "+Back.RESET+Fore.RESET+"Prompt: -->   ").lower()
    print(Back.CYAN+'                            \n')

    # Part 1: Creating a clearer prompt for the AI
    prompt1 = "You are going to make this prompt clearer for an AI Professional Developer to create a code using " + coding_language + ". Make a better prompt for this:" + initial_input
    generated_text, token_count1 = create_code_with_prompt(prompt1, max_tokens=200)

    # Part 2: Asking a follow-up question for clarification
    prompt2 = 'You are an AI which needs to create 1 follow-up question (1 sentence no breaks, ex: Does the game need a something , Does the website need modern css?, etc ) for the following prompt to clarify for the AI which will then create a certain code later on, if there are no questions then say: "No Questions Generated, please input "none"", prompt:' + generated_text
    follow_up_question, token_count2 = create_code_with_prompt(prompt2, max_tokens=200)
    user_answer = input(Back.RESET+"\n"+follow_up_question.strip() + " --> ")

    # Part 3: Generating the final code with additional clarifications
    final_input = "Your are a Professional  Developer and you need to give a " + coding_language + " code to the following prompt, here are additional clarifications," + "Follow-up question: " + follow_up_question + "User's answer: " + user_answer + "This is the prompt:" + generated_text
    generated_text_2, token_count3 = create_code_with_prompt(final_input, max_tokens=4000)

    total_tokens_used = token_count1 + token_count2 + token_count3

    print("\n\nPlease wait a minute...\n\n" + coding_language + " Code file is being created...\nProcess can take around 3-20 seconds.")
    loading_animation(3)

    print(Fore.BLACK + Back.MAGENTA + "Improved Prompt by AI:" + generated_text + Back.CYAN + '\nGenerated Code:' + generated_text_2)
    print(f"Total tokens used: {total_tokens_used}")

    user_choice = input(Back.BLACK + Style.BRIGHT + "Do you want to save this code to a file? (y/n) -->  ").lower().strip(",-+×÷=/_<>[]!@$%^&*()-:;,?.")
    if user_choice == "y":
        save_to_file(generated_text_2)
    else:
        print("Goodbye! Code is not saved. Feel free to generate and preview another.")

if __name__ == "__main__":
    main()
