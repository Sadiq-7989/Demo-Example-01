import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the client. It automatically picks up GEMINI_API_KEY from the environment.
try:
    client = genai.Client()
except ValueError:
    client = None
    print("Warning: GEMINI_API_KEY is missing. UI will load, but AI features will not work until the key is set.")

MODEL_ID = 'gemini-2.5-flash'

def chat_stream(history, message):
    """
    Generator that streams the response for the chat interface.
    `history` is a list of dicts like: [{"role": "user", "content": "hello"}, ...]
    """
    # Convert Gradio history into the format expected by google-genai if needed
    # Actually google-genai chat sessions handle history elegantly.
    
    # Initialize chat session
    chat = client.chats.create(model=MODEL_ID)
    
    # Send all history messages to the chat (excluding the last one which is the new message)
    # But wait, Gradio passes the entire history to the function if configured correctly,
    # or just the history so far. If using the new Gradio ChatInterface or Chatbot, 
    # we just need to reconstruct the session history.
    
    # Let's rebuild the history for the genai client
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })
        
    chat = client.chats.create(
        model=MODEL_ID,
        config={"system_instruction": "You are a helpful AI Workspace Pro assistant."}
    )
    
    # To maintain history in the actual chat session object, we could pass it in
    # However, google-genai doesn't easily initialize history in one shot like this.
    # Alternatively, we just use standard generation with a concatenated prompt, 
    # or use `client.models.generate_content_stream` with the full contents array.
    
    contents = formatted_history + [{"role": "user", "parts": [{"text": message}]}]
    
    response_stream = client.models.generate_content_stream(
        model=MODEL_ID,
        contents=contents,
        config={"system_instruction": "You are a helpful AI Workspace Pro assistant. Be concise and professional."}
    )
    
    partial_text = ""
    for chunk in response_stream:
        if chunk.text:
            partial_text += chunk.text
            yield partial_text


def summarize(text, length, style):
    """
    Generate a summary of the provided text.
    """
    prompt = f"""
    Please summarize the following text.
    Target length: {length}
    Format style: {style}
    
    Text to summarize:
    {text}
    """
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return response.text


def generate_ideas(topic, tone):
    """
    Generate 3 distinct ideas based on the topic and tone.
    """
    prompt = f"""
    Brainstorm 3 distinct ideas about the following topic.
    Topic: {topic}
    Tone: {tone}
    
    Format the response strictly as exactly 3 ideas separated by "---IDEA_SEPARATOR---".
    For example:
    Idea 1 description
    ---IDEA_SEPARATOR---
    Idea 2 description
    ---IDEA_SEPARATOR---
    Idea 3 description
    
    Do not use any markdown bolding for the separator, just the exact text.
    """
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    
    raw_text = response.text
    # Split the ideas
    ideas = raw_text.split("---IDEA_SEPARATOR---")
    
    # Clean up whitespace
    ideas = [idea.strip() for idea in ideas if idea.strip()]
    
    # Pad to 3 ideas just in case the model outputs fewer
    while len(ideas) < 3:
        ideas.append("Could not generate an idea. Please try again.")
        
    # Return exactly the first 3
    return ideas[:3]
