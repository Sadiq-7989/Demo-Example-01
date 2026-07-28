import gradio as gr
from utils.gemini_client import generate_ideas
from utils.theme import UI_CLASSES, ICONS
from components.universal_input import create_universal_input

def create_idea_generator_view():
    with gr.Column(visible=False, elem_classes="page-content") as view:
        gr.Markdown(f"# {ICONS.IDEAS} Idea Generator", elem_classes=UI_CLASSES.HEADING_LG)
        gr.Markdown("Brainstorm topics, content strategies, and project concepts instantly.", elem_classes=UI_CLASSES.TEXT_SUBTITLE)
        
        with gr.Row():
            with gr.Column(scale=1, elem_classes=UI_CLASSES.PREMIUM_CARD):
                gr.Markdown("### Topic & Tone", elem_classes=UI_CLASSES.HEADING_MD)
                tone = gr.Dropdown(["Professional", "Creative", "Academic", "Humorous"], value="Professional", label="Select Tone")
                
                # Universal Input
                text_input, pdf_input, voice_input, image_input, submit_btn = create_universal_input()
                
            with gr.Column(scale=2, elem_classes=[UI_CLASSES.GLASS_PANEL, "pad-6"]):
                gr.Markdown("### Generated Ideas", elem_classes=UI_CLASSES.HEADING_MD)
                
                with gr.Column():
                    idea_1 = gr.Markdown("1. Output will appear here...", elem_classes="text-primary")
                    gr.HTML("<hr style='border-color: var(--border-color); opacity: 0.5;'>")
                    idea_2 = gr.Markdown("2. Output will appear here...", elem_classes="text-primary")
                    gr.HTML("<hr style='border-color: var(--border-color); opacity: 0.5;'>")
                    idea_3 = gr.Markdown("3. Output will appear here...", elem_classes="text-primary")
                
        # Events
        submit_btn.click(generate_ideas, inputs=[text_input, tone], outputs=[idea_1, idea_2, idea_3])
        
    return view
