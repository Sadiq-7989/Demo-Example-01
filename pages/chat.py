import gradio as gr
from utils.gemini_client import chat_stream
from utils.theme import UI_CLASSES, ICONS
from components.universal_input import create_universal_input

def user(user_message, history):
    # If the user message is from text input
    if user_message:
        return "", history + [{"role": "user", "content": user_message}]
    return "", history

def bot(history):
    if not history:
        yield history
        return
        
    user_message = history[-1]["content"]
    history.append({"role": "assistant", "content": ""})
    previous_history = history[:-2]
    
    for chunk in chat_stream(previous_history, user_message):
        history[-1]["content"] = chunk
        yield history

def create_chat_view():
    with gr.Column(visible=False, elem_classes="page-content") as view:
        gr.Markdown(f"# {ICONS.CHAT} AI Assistant", elem_classes=UI_CLASSES.HEADING_LG)
        gr.Markdown("Chat with your advanced AI model.", elem_classes=UI_CLASSES.TEXT_SUBTITLE)
        
        with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD):
            chatbot = gr.Chatbot(
                value=[{"role": "assistant", "content": "Hello! I am your AI Workspace Pro assistant. How can I help you today?"}],
                elem_classes="chat-window",
                show_label=False
            )
            
            # Use universal input component
            text_input, pdf_input, voice_input, image_input, submit_btn = create_universal_input()
                
        # Real interactions connected to Gemini AI via Text Input
        text_input.submit(user, [text_input, chatbot], [text_input, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        submit_btn.click(user, [text_input, chatbot], [text_input, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        
    return view
