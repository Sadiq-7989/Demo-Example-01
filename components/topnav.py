import gradio as gr
from utils.theme import ICONS
from components.profile_widget import create_profile_widget

def create_topnav():
    with gr.Row(elem_classes="topnav"):
        with gr.Column(scale=1, min_width=350):
            # Global Search Bar
            gr.Textbox(
                placeholder=f"{ICONS.SEARCH} Search chats, PDFs, ideas...",
                show_label=False,
                container=False,
                elem_classes="search-bar"
            )
        
        with gr.Row(scale=1):
            gr.HTML("<div style='flex-grow: 1'></div>") # Spacer
            
            # Status Indicator
            gr.HTML(f"""
            <div style="display: flex; align-items: center; gap: 1.5rem; height: 100%;">
                <div class="status-badge">
                    <div class="status-dot"></div> Gemini Connected
                </div>
                <div style="font-size: 1.25rem; cursor: pointer; color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-secondary)'">
                    {ICONS.NOTIFICATIONS}
                </div>
                <div style="font-size: 1.25rem; cursor: pointer; color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-secondary)'">
                    {ICONS.THEME}
                </div>
            </div>
            """)
            
            # Profile Avatar (simple trigger or embedded)
            with gr.Accordion("Profile", open=False):
                create_profile_widget()
