import os
import anthropic
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the output folder path
output_folder_path = r"CHOOSE OUTPUT FOLDER"

# Authenticate with the Anthropic API using your API key
client = anthropic.Client(api_key="YOUR CLAUDE 3 Haiku API")

# Specify the Claude model to use
model = "claude-3-haiku-20240307"

def make_api_call(prompt):
    messages = [{"role": "user", "content": prompt}]
    
    try:
        logging.info("Connecting to API")
        response = client.messages.create(
            model=model,
            messages=messages,
            max_tokens=4000,
            stop_sequences=["\n\nHuman:"],
        )
        result = response.content[0].text
        logging.info("Successfully connected to API")
        return result
    except Exception as e:
        logging.error(f"API request failed: {str(e)}")
        return None

def save_to_txt(result, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as txtfile:
            txtfile.write(result)
        
        logging.info(f"Saved response to TXT: {output_file}")
    except Exception as e:
        logging.error(f"Error saving to TXT: {str(e)}")

def main():
    # Your prompt that will generate a txt response
    prompt = """Create a list of 50 titles for articles in the NICHE niche and the specific topics can be around TOPIC 1 and TOPIC 2
    """
    
    # Make API call 5 times
    for i in range(1, 6):
        result = make_api_call(prompt)

        # Save the result to TXT
        if result:
            output_file = os.path.join(output_folder_path, f"output_response{i}.txt")
            save_to_txt(result, output_file)

    logging.info("Process completed.")

if __name__ == "__main__":
    main()