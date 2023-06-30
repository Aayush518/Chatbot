import streamlit as st
import csv

# Load the pairs from the CSV file
def load_pairs(filename):
    pairs = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            pairs.append(row)
    return pairs

# Define a function to find the response given a question
def get_response(question):
    for pair in pairs:
        if question.lower() == pair[0].lower():
            return pair[1]
    return "I'm sorry, I don't have an answer for that."

# Load the pairs from the CSV file
pairs = load_pairs('conversation_pairs.csv')

# Create the Streamlit app
def main():
    st.title("Chatbot")

    # User input
    user_input = st.text_input("User:")
    
    # Check if user input is not empty
    if user_input:
        # Get response
        response = get_response(user_input)

        # Display the response
        st.text("Chatbot: " + response)

if __name__ == "__main__":
    main()
