import gradio as gr

# Load Components
from components.sidebar import create_sidebar
from components.topnav import create_topnav
from components.footer import create_footer

# Load Pages
from pages.login import create_login_view
from pages.home import create_home_view
from pages.chat import create_chat_view
from pages.summarizer import create_summarizer_view
from pages.idea_generator import create_idea_generator_view
from pages.dashboard import create_dashboard_view

# Load Theme
from utils.theme import get_gradio_theme

# Load custom CSS
with open("assets/style.css", "r", encoding="utf-8") as f:
    custom_css = f.read()

def change_view(view_name):
    """
    Returns updates for visibility of views and active states of sidebar buttons.
    Order: [Home, Chat, Summarizer, Ideas, Dashboard] views
           [Home, Chat, Summarizer, Ideas, Dashboard] buttons
    """
    # Visibility logic
    views = {
        "home": [True, False, False, False, False],
        "chat": [False, True, False, False, False],
        "summarizer": [False, False, True, False, False],
        "ideas": [False, False, False, True, False],
        "dashboard": [False, False, False, False, True]
    }
    
    # Active button logic
    active_cls = ["sidebar-btn", "active"]
    inactive_cls = "sidebar-btn"
    
    buttons = {
        "home": [gr.update(elem_classes=active_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls)],
        "chat": [gr.update(elem_classes=inactive_cls), gr.update(elem_classes=active_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls)],
        "summarizer": [gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=active_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls)],
        "ideas": [gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=active_cls), gr.update(elem_classes=inactive_cls)],
        "dashboard": [gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=inactive_cls), gr.update(elem_classes=active_cls)]
    }
    
    visibility = [gr.update(visible=v) for v in views[view_name]]
    return visibility + buttons[view_name]

def handle_login():
    """Switches from Login View to Main App View"""
    return gr.update(visible=False), gr.update(visible=True)

def handle_logout():
    """Switches from Main App View back to Login View"""
    return gr.update(visible=True), gr.update(visible=False)

with gr.Blocks() as demo:
    
    # --- LOGIN SCREEN ---
    view_login, btn_login = create_login_view()
    
    # --- MAIN APPLICATION (Hidden Initially) ---
    with gr.Row(visible=False, elem_classes="app-wrapper") as main_app:
        
        # Left Sidebar
        btn_home, btn_chat, btn_summarizer, btn_ideas, btn_dashboard, btn_settings, btn_logout = create_sidebar()
        
        # Right Main Column
        with gr.Column(elem_classes="main-column"):
            # Top Navigation
            create_topnav()
            
            # Dynamic Page Container
            view_home = create_home_view()
            view_chat = create_chat_view()
            view_summarizer = create_summarizer_view()
            view_ideas = create_idea_generator_view()
            view_dashboard = create_dashboard_view()
            
            # Spacer to push footer to bottom
            gr.HTML("<div style='flex-grow: 1'></div>")
            
            # Footer
            create_footer()

    # --- EVENTS & ROUTING ---
    
    # Login & Logout
    btn_login.click(handle_login, inputs=None, outputs=[view_login, main_app])
    btn_logout.click(handle_logout, inputs=None, outputs=[view_login, main_app])
    
    # Sidebar Navigation Routing
    all_views = [view_home, view_chat, view_summarizer, view_ideas, view_dashboard]
    all_btns = [btn_home, btn_chat, btn_summarizer, btn_ideas, btn_dashboard]
    nav_outputs = all_views + all_btns
    
    btn_home.click(lambda: change_view("home"), None, nav_outputs)
    btn_chat.click(lambda: change_view("chat"), None, nav_outputs)
    btn_summarizer.click(lambda: change_view("summarizer"), None, nav_outputs)
    btn_ideas.click(lambda: change_view("ideas"), None, nav_outputs)
    btn_dashboard.click(lambda: change_view("dashboard"), None, nav_outputs)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, css=custom_css, theme=get_gradio_theme())
