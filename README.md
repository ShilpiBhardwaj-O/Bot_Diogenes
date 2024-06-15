# Bot_Diogenes
The provided code implements a simple chatbot named Diogenes using Python. Here's a detailed description of what the code does and how it works:

1. Import Libraries: The code begins by importing necessary libraries, including numpy, string, random, spacy, and modules from sklearn.

2. Load Language Model: It loads the English language model from spaCy. This model is used for tokenization and other NLP tasks.

3. Read and Tokenize Text: The code reads a text file 'dio_bot.txt' and processes it using spaCy. It tokenizes the text into sentences and words. Each sentence is added to a list called `sentences`, and each word is added to a list called `words`.

4. Text Preprocessing: It defines a function `lemmatize` to lemmatize the words in a given text. Lemmatization reduces words to their base or root form (e.g., "running" to "run").

5. Greeting Function: The code defines a function `greet` that takes a sentence as input and returns a random greeting from a predefined list if the sentence contains a greeting word.

6. Generate Responses: It defines a function `respond` that generates responses based on user input. It uses TF-IDF vectorization to convert text into numerical vectors and cosine similarity to find the most similar sentence in the corpus to the user input.

7. Conversation Loop: The code initiates a conversation with the user. It prints a greeting from Diogenes and prompts the user to input text. It then processes the user input to determine if it is a greeting, a thank you message, or a regular statement. Based on the input, it generates and prints a response from Diogenes.

8. End Conversation: The conversation continues until the user inputs 'bye', at which point the code prints a closing message and ends the conversation.

Here's a summary of what the chatbot does:

1. Respond to Greetings: When the user greets the chatbot, it responds with a random greeting from a predefined list.

2. Answers Questions: The chatbot uses TF-IDF vectorization and cosine similarity to find the most similar sentence in its training corpus to the user's input. It then responds with that sentence, which is intended to be an answer or a relevant response to the user's query.

3. Handles Thank You Messages: If the user thanks the chatbot, it responds with a polite acknowledgement.

4. Ends Conversations: The chatbot can end the conversation when the user inputs 'bye'. It prints a closing message and exits the conversation loop.
