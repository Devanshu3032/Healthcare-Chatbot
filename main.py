import json
import re
import random_responses  # Ensure this module exists or remove it

def load_json(file):
    try:
        with open(file, 'r') as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{file}'.")
        return []

responses_data = load_json("bot.json")

def get_response(input_string):
    if not input_string.strip():
        return "Please type something so we can chat :)"
        
    # Convert user input to lowercase and split into words
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    
    for response in responses_data:
        # Convert required words and user inputs to lowercase
        required_words = [word.lower() for word in response.get("required_words", [])]
        user_inputs = [word.lower() for word in response["user_input"]]
    
        # Check if all required words are present in the user's input
        if all(word in split_message for word in required_words):
            # Calculate score based on matching words in user_inputs
            score = sum(word in split_message for word in user_inputs)
            score_list.append(score)
        else:
            # No match if required words are missing
            score_list.append(0)
    
    # Find the best matching response
    best_score = max(score_list)
    response_index = score_list.index(best_score)
    
    if best_score > 0:
        return responses_data[response_index]["bot_response"]
    else:
        return random_responses.random_string()  # Use your random response function
  # Replace with random_responses if needed

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))