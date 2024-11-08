from dotenv import load_dotenv
import os
import json
from groq import Groq # type: ignore 

load_dotenv()

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY')
)

def draft_url(content, role='user'):
    return {
        'role': role,
        'content': content
    }

def generate_qna(content):
    cont = content

    messages = [
        {
            'role': 'system',
            'content' : 'generates 5 questions and multiple-choice options that help categorize users visiting the site in JSON'
        }
    ]
    messages.append(draft_url(content))
    chat_completion = client.chat.completions.create(
        temperature=1.0,
        n=1,
        model="llama3-8b-8192",
        messages=messages,
        response_format={"type": "json_object"},
    )
    return chat_completion.choices[0].message.content
    return response_json