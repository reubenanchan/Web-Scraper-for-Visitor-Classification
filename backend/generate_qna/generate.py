from typing import List
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
#from groq import Groq # type: ignore
from openai import OpenAI
import instructor 
from jsonify import convert
from flask import jsonify
#from json_class import QuestionModel

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class QuestionModel(BaseModel):
    question: str
    choices: list[str]
    
class QuestionList(BaseModel):
    title: str
    question_bank: list[QuestionModel]

def draft_url(content, role='user'):
    return {
        'role': role,
        'content': content
    }

def generate_qna(content):
    messages = [
        {
            "role": "system", 
            "content": "generates 5 questions and multiple-choice options that help categorize users visiting the site"
        }
    ]
    messages.append(draft_url(content))
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=messages,
        response_format=QuestionList,
    )
    output = completion.choices[0].message.parsed

    return output.question_bank
