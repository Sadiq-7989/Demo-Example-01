import gradio as gr
from utils.theme import ICONS, UI_CLASSES

def create_profile_widget():
    """Creates a user profile widget for the top navigation or sidebar."""
    with gr.Column(elem_classes="profile-widget", scale=1):
        with gr.Row(elem_classes="profile-header"):
            gr.HTML(f"""
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary)); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.2rem;">
                    S
                </div>
                <div>
                    <div style="font-weight: 600; font-size: 0.95rem;">Sadiq</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">sadiq@example.com</div>
                </div>
            </div>
            """)
        
        with gr.Row():
            gr.HTML(f"""
            <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem;">
                    <span style="color: var(--text-secondary);">Model</span>
                    <span style="font-weight: 600; color: var(--accent-primary);">Gemini 2.5 Pro</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem;">
                    <span style="color: var(--text-secondary);">Last Login</span>
                    <span>Just now</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem;">
                    <span style="color: var(--text-secondary);">Status</span>
                    <span class="status-badge"><div class="status-dot"></div> Online</span>
                </div>
            </div>
            """)
