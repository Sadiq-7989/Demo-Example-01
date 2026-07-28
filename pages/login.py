import gradio as gr
from utils.theme import UI_CLASSES, LABELS

def create_login_view():
    """Creates the premium glassmorphism login view."""
    with gr.Column(visible=True, elem_id="login-view") as view:
        # Full screen background with gradient
        with gr.Column(elem_classes="app-wrapper"):
            gr.HTML(f"""
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.15) 0%, var(--bg-base) 100%); z-index: 0;"></div>
            """)
            
            with gr.Column(scale=1):
                gr.HTML("<div style='height: 15vh;'></div>")
                
                with gr.Row():
                    gr.HTML("<div style='flex-grow: 1'></div>")
                    with gr.Column(scale=2, min_width=400, elem_classes=UI_CLASSES.GLASS_PANEL):
                        gr.Markdown(f"<h1 style='text-align: center; margin-bottom: 0;' class='text-gradient'>{LABELS.APP_NAME}</h1>")
                        gr.Markdown(f"<p style='text-align: center; color: var(--text-secondary); margin-bottom: 2rem;'>{LABELS.APP_SUBTITLE}</p>")
                        
                        email = gr.Textbox(placeholder="Email address", show_label=False, container=False, elem_classes=UI_CLASSES.UNIVERSAL_INPUT)
                        password = gr.Textbox(placeholder="Password", type="password", show_label=False, container=False, elem_classes=UI_CLASSES.UNIVERSAL_INPUT)
                        
                        with gr.Row():
                            remember = gr.Checkbox(label="Remember me", value=True)
                            forgot = gr.HTML("<a href='#' style='color: var(--accent-primary); font-size: 0.85rem; text-decoration: none;'>Forgot password?</a>")
                        
                        btn_login = gr.Button("Sign In", elem_classes=UI_CLASSES.BTN_PRIMARY)
                        
                        gr.HTML("<div style='text-align: center; margin-top: 1.5rem; font-size: 0.85rem; color: var(--text-secondary);'>Don't have an account? <a href='#' style='color: var(--text-primary); text-decoration: none;'>Register</a></div>")
                    gr.HTML("<div style='flex-grow: 1'></div>")
                    
    return view, btn_login
