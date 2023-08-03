# aicreate - generate codes using the power of AI.

This script is designed to help you generate codes using an AI-powered prompt and OpenAI's text-davinci-003 engine. It interactively takes your input, refines the prompt, generates follow-up questions, and ultimately provides a code based on the given information.

## Requirements

To run this script, make sure you have Python installed, and you can install the necessary dependencies by running: 'pip install -r requirements.yml' in the Shell terminal. You can also just run the repl and it will automatically download the dependencies.

## How to Use This Repl?

1. Run the script.
2. Enter your OpenAI API key when prompted.
3. Choose the coding language you want for the generated code.
4. Provide an initial prompt that the AI will use.
5. The AI will suggest a clearer prompt based on your input and ask you a follow-up question for clarification.
6. Respond to the follow-up question.
7. The AI will then generate a more detailed prompt and use it to create the code.
8. Wait for the code to be generated. Usually takes 3-20 seconds.
9. Preview the improved prompt and the generated code.
10. Optionally, you can choose to save the generated code to a filename of your choice.

## Output

The output will consist of the improved prompt and the generated code all by AI. You can choose to save the code to a file if you want to.

## Important Notes

- The generated code is created based on the provided prompt and follow-up question. The accuracy and quality of the code may vary depending on the clarity and specificity of the input.
- I do not save your OpenAI API keys.
- The `text-davinci-003` engine is used for text completion, and the prompt generation process may differ based on the availability of the engine and your API usage limits.

Feel free to experiment with different prompts and follow-up questions to get the best results from the AI. Later on, I will add the ability to loop so if the generated preview is not to your liking it can regenerate a response.

Have fun generating code! If you have any questions or encounter any issues, feel free to contact seth@minister.com or seek support from the OpenAI community. Enjoy!
