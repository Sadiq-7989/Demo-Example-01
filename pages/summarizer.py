import gradio as gr
from utils.gemini_client import summarize
from utils.theme import UI_CLASSES, ICONS
from components.universal_input import create_universal_input

def create_summarizer_view():
    with gr.Column(visible=False, elem_classes="page-content") as view:
        gr.Markdown(f"# {ICONS.SUMMARIZE} Document Summarizer", elem_classes=UI_CLASSES.HEADING_LG)
        gr.Markdown("Upload large documents or paste text to get instant intelligent summaries.", elem_classes=UI_CLASSES.TEXT_SUBTITLE)
        
        with gr.Row():
            with gr.Column(scale=1, elem_classes=UI_CLASSES.PREMIUM_CARD):
                gr.Markdown("### Input", elem_classes=UI_CLASSES.HEADING_MD)
                
                # Configuration
                length = gr.Radio(["Short", "Medium", "Detailed"], value="Medium", label="Summary Length")
                style = gr.Dropdown(["Bullet Points", "Paragraphs", "Executive Summary"], value="Bullet Points", label="Format Style")
                
                # Universal Input
                text_input, pdf_input, voice_input, image_input, submit_btn = create_universal_input()
                
            with gr.Column(scale=1, elem_classes=UI_CLASSES.PREMIUM_CARD):
                gr.Markdown("### Output", elem_classes=UI_CLASSES.HEADING_MD)
                output = gr.Markdown("Your summary will appear here...", elem_classes="text-primary")
                
        # Events
        submit_btn.click(summarize, inputs=[text_input, length, style], outputs=output)
        
    return view
