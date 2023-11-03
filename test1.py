import json
import spacy
import string

# Load data from the "scraped_data.json" file
with open('scraped_data.json', 'r') as file:
    data = json.load(file)

# Extract the text data from the JSON file, checking for the 'text' key
text_data = [entry.get('text', '') for entry in data]

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define functions for text preprocessing
def preprocess_text(text):
    doc = nlp(text)
    preprocessed_tokens = []
    
    for token in doc:
        # Remove punctuation and numbers
        if not token.is_punct and not token.is_digit:
            # Convert to lowercase and lemmatize
            preprocessed_tokens.append(token.lemma_.lower())

    return preprocessed_tokens

# Apply preprocessing to the text data
preprocessed_data = [preprocess_text(text) for text in text_data]

# Save the preprocessed text data to a file or database
# You can save it as a list or in your preferred format
# Example: Save preprocessed data to a text file
with open('preprocessed_text_data.txt', 'w') as file:
    for item in preprocessed_data:
        file.write("%s\n" % ' '.join(item))