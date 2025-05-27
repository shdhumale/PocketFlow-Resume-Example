# utils.py
# from openai import OpenAI
# import os

# #OPENAI_API_KEY = "<YOIUR_API_KEY>";
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# #client = OpenAI(OPENAI_API_KEY)

# def call_llm(prompt):
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content

# import requests
# import json

# def call_llm(prompt):
#     response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": "Bearer <YOUR_API_KEY>",
#     "Content-Type": "application/json",
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   data=json.dumps({
#     "model": "meta-llama/llama-3.3-8b-instruct:free",
#     "messages": [{"role": "user", "content": prompt}],
    
#   })
# )
#     print("response.text", response.text)
#     print("response.text", response.content)
    
#     return response.content

import google.generativeai as genai
import google.generativeai.types as types
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')


# Generate content
# chat = model.start_chat()
# response = chat.send_message("Write a short story about a cat.")
# print(response.text)

def call_llm(prompt):
    
    response = model.generate_content([
       {"role": "user", "parts": [prompt]}
   ], stream=False)
    print(response.text)
    return response.text
