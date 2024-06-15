#Diogens
import numpy as np  # Import numpy for numerical operations
import string  # Import string for string operations
import random  # Import random for random number generation
from sklearn.feature_extraction.text import TfidfVectorizer  # Import TfidfVectorizer from sklearn for TF-IDF vectorization
from sklearn.metrics.pairwise import cosine_similarity  # Import cosine_similarity from sklearn for computing cosine similarity
import spacy  # Import spacy for NLP operations

# Load the English model from spaCy
philosopher = spacy.load('en_core_web_sm')

# Read and process the text file
with open('dio_bot.txt', 'r', errors='ignore') as f:  # Open the file 'dio_bot.txt' in read mode
    raw_dialogue = f.read().lower()  # Read the content of the file and convert it to lowercase

# Tokenize the sentences and words using spaCy
sentences = [sentence.text for sentence in philosopher(raw_dialogue).sents]  # Tokenize the text into sentences
words = [word.text.lower() for word in philosopher(raw_dialogue)]  # Tokenize the text into words

# Text Preprocessing
def lemmatize(text):
    """Lemmatize the given text"""
    return [token.lemma_ for token in philosopher(text) if token.is_alpha]  # Lemmatize the text

# Defining the greeting function
GREETING_WORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "howdy", "henlo", "namaste", "salam", 'how are you?')
GREETING_RESPONSES = [
    "Well, it took you long enough.",
    "Greetings. Do you have a purpose, or are you simply wasting air?",
    "What do you want?",
    "How can I help you, fellow biped?",
    "Why bother with greetings? We'll all be dust soon anyway.",
    "Speak your mind, friend.",
    "Ah, another soul lost in the marketplace. To what do I owe this visit?",
    "(Raises an eyebrow) You seem surprised. Did you not expect to find someone here?",
    "(While looking for lice) Greetings! Have you come to join my delightful companions?",
    "(Nods silently) Oh, a biped!",
    "A simple greeting suffices."
]

def greet(sentence):
    """Responds with a random greeting if the input contains a greeting word"""
    for word in sentence.split():
        if word.lower() in GREETING_WORDS:
            return random.choice(GREETING_RESPONSES)  # Return a random greeting response
    return None

# Generate responses for user inputs
def respond(user_input):
    """Generates a response based on the input using TF-IDF vectorization and cosine similarity"""
    bot_response = ''
    sentences.append(user_input)  # Add the user input to the list of sentences

    tfidf_vectorizer = TfidfVectorizer(tokenizer=lemmatize, stop_words='english')  # Initialize the TfidfVectorizer
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)  # Fit the vectorizer and transform the sentences into TF-IDF matrix

    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])  # Calculate cosine similarities
    idx = np.argmax(similarities)  # Get the index of the most similar sentence
    flat = similarities.flatten()  # Flatten the similarities matrix
    flat.sort()  # Sort the flattened similarities

    similarity_score = flat[-2]  # Get the similarity score

    if similarity_score == 0:
        bot_response = bot_response + "I am sorry. I don't understand you."  # Add default response if no similarity
    else:
        bot_response = bot_response + sentences[idx]  # Add the most similar sentence as the response

    sentences.pop(-1)  # Remove the user response added for similarity computation
    return bot_response

# Initiating and ending the conversation
dialogue_ongoing = True  # Set the conversation flag to True
print("""Diogenes: My name is... what does it matter? 
Let's have a conversation, if you can manage something more stimulating than mindless chatter.
By the way, typing 'bye' is the only escape from this inevitable tedium.""")

while dialogue_ongoing:
    user_input = input().lower()  # Take user input and convert it to lowercase
    if user_input != 'bye':
        if user_input in ('thanks', 'thank you'):  # Check if user input is a thank you message
            dialogue_ongoing = False  # End the conversation
            print("Diogenes: You are Welcome..")  # Print a thank you response
        else:
            if any(word.lower() in user_input.split() for word in GREETING_WORDS):  # Check if user input is a greeting
                print("Diogenes: " + greet(user_input))  # Respond with a greeting
            else:
                print("Diogenes: ", end="")  # Print the bot's response
                print(respond(user_input))  # Generate and print the bot's response based on the user input
    else:
        dialogue_ongoing = False  # End the conversation
        print("Diogenes: Off you go then. Remember, all things are fleeting, even tedious conversations.")  # Print a closing message
