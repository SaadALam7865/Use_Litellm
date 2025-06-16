import os
from litellm import Agent
from dotenv import load_dotenv
from litellm import completion
# load environment variables from .env file

load_dotenv()
def main():
    # Get the APi key from the environment variable
    api_key  = os.getenv('GEMINI_API_KEY')
    
    response = completion(
        model='gemini/gemini-2.0-flash',
        messages=[{
            'role': 'user',
            'content': 'who is the third caliph of Islam?'
        }]
    )
   

    print(response['choices'][0]['message']['content'])


if __name__ == '__main__':
        main()
