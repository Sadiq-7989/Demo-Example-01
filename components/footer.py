import gradio as gr
from utils.theme import LABELS

def create_footer():
    """Creates a footer component to be placed at the bottom of the main layout."""
    gr.HTML(f"""
    <div style="text-align: center; padding: 2rem; color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid var(--border-color); margin-top: auto;">
        <div style="font-weight: 600; color: var(--text-secondary); margin-bottom: 0.25rem;">
            {LABELS.APP_NAME} <span style="font-weight: normal;">- {LABELS.VERSION}</span>
        </div>
        <div>{LABELS.POWERED_BY} &bull; Built with Gradio</div>
    </div>
    """)
