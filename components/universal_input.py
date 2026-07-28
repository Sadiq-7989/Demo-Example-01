import gradio as gr
from utils.theme import UI_CLASSES, ICONS

def create_universal_input():
    """
    Creates a universal input block that supports:
    - Text Prompts
    - PDF Uploads
    - Voice Recording
    - Image Uploads
    Returns the elements for hooking up events.
    """
    with gr.Column(elem_classes=UI_CLASSES.UNIVERSAL_INPUT):
        with gr.Tabs():
            with gr.TabItem(f"{ICONS.CHAT} Text"):
                text_input = gr.Textbox(
                    placeholder="Type your message, prompt, or task here...",
                    show_label=False,
                    container=False,
                    lines=3
                )
            with gr.TabItem(f"{ICONS.PDF} Document"):
                pdf_input = gr.File(
                    label="Upload PDF or Document",
                    file_types=[".pdf", ".docx", ".txt"]
                )
            with gr.TabItem(f"{ICONS.VOICE} Voice"):
                voice_input = gr.Audio(
                    label="Record or Upload Audio",
                    type="filepath"
                )
            with gr.TabItem(f"{ICONS.IMAGE} Image (Soon)"):
                image_input = gr.Image(
                    label="Upload Image for Analysis",
                    type="filepath"
                )
        
        with gr.Row():
            gr.HTML("<div style='flex-grow: 1'></div>")
            submit_btn = gr.Button("🚀 Send to Gemini", elem_classes=UI_CLASSES.BTN_PRIMARY)
            
    return text_input, pdf_input, voice_input, image_input, submit_btn
