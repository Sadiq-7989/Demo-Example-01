import gradio as gr
from utils.theme import ICONS, LABELS, UI_CLASSES

def create_sidebar():
    with gr.Column(elem_classes="sidebar-container"):
        with gr.Column(elem_classes="sidebar-logo-container"):
            gr.Markdown(f"# {LABELS.APP_NAME}", elem_classes="text-gradient", elem_id="sidebar-logo")
            gr.Markdown(f"**{LABELS.VERSION}** &bull; {LABELS.POWERED_BY}", elem_classes="text-xs text-muted")
        
        with gr.Column(elem_classes="sidebar-nav"):
            # Current Features
            gr.Markdown(f"### {LABELS.CORE_FEATURES}", elem_classes="text-xs text-muted", elem_id="sidebar-group-1")
            btn_home = gr.Button(f"{ICONS.HOME} Dashboard", elem_classes=UI_CLASSES.SIDEBAR_BTN_ACTIVE)
            btn_chat = gr.Button(f"{ICONS.CHAT} AI Chat", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_summarizer = gr.Button(f"{ICONS.SUMMARIZE} Summarizer", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_ideas = gr.Button(f"{ICONS.IDEAS} Idea Generator", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_dashboard = gr.Button(f"{ICONS.DASHBOARD} Analytics", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            
            gr.HTML("<hr style='border-color: var(--border-color); margin: 1rem 0;'>")
            
            # Future Features
            gr.Markdown(f"### {LABELS.UPCOMING}", elem_classes="text-xs text-muted", elem_id="sidebar-group-2")
            btn_resume = gr.Button(f"{ICONS.RESUME} Resume Analyzer (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_image = gr.Button(f"{ICONS.IMAGE} Image Analyzer (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_code = gr.Button(f"{ICONS.CODE} Code Generator (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_email = gr.Button(f"{ICONS.EMAIL} Email Writer (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_presentation = gr.Button(f"{ICONS.PRESENTATION} Presentation (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_research = gr.Button(f"{ICONS.RESEARCH} Research Assistant (Soon)", elem_classes=UI_CLASSES.SIDEBAR_BTN)
        
        with gr.Column(elem_classes="sidebar-footer"):
            btn_settings = gr.Button(f"{ICONS.SETTINGS} Settings", elem_classes=UI_CLASSES.SIDEBAR_BTN)
            btn_logout = gr.Button("🚪 Logout", elem_classes=UI_CLASSES.SIDEBAR_BTN)
        
        return btn_home, btn_chat, btn_summarizer, btn_ideas, btn_dashboard, btn_settings, btn_logout
