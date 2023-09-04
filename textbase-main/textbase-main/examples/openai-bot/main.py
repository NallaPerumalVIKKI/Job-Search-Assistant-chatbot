from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = ""

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like.
The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a
pleasant chat!
"""

@bot()
# Import the OpenAI library
import openai

# Set your OpenAI API key
api_key = "your_api_key_here"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to process the response from GPT-3
def process_response(response):
    return response.choices[0].text.strip()

# Function to analyze job search queries
def analyze_job_search(query):
    # Construct a prompt for job search analysis
    prompt = f"Please provide information related to the job search for the following query: {query}"
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the response
    result = process_response(response)
    
    return result

# Function to compare job listings
def compare_job_listings(job_titles):
    # Construct a prompt for comparing job listings
    prompt = f"Compare the following job listings: {', '.join(job_titles)}"
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the comparison information
    result = process_response(response)
    
    return result

# Function to provide job listings
def provide_job_listings(location, job_type):
    # Construct a prompt for providing job listings
    prompt = f"Please provide me with job listings in {location} for {job_type} positions."
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the job listings
    result = process_response(response)
    
    return result

# Function to provide resume tips
def provide_resume_tips():
    # Construct a prompt for resume tips
    prompt = "Please share some tips for improving a resume."
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the resume tips
    result = process_response(response)
    
    return result

# Function to provide interview tips
def provide_interview_tips():
    # Construct a prompt for interview tips
    prompt = "Please offer advice on having a successful job interview."
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the interview tips
    result = process_response(response)
    
    return result

# Function to provide career advice
def provide_career_advice():
    # Construct a prompt for career advice
    prompt = "Please give me some general career advice or guidance."
    
    # Call GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Process and format the career advice
    result = process_response(response)
    
    return result
















def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }