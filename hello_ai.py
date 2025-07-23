import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from .env file
load_dotenv()

# Configure the API client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Make the API call
response = model.generate_content("Write a short, inspiring quote about learning.")

# Print the AI's response
print(response.text)