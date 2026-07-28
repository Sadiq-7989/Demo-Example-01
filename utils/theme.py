"""
Centralized Theme Configuration for AI Workspace Pro
Stores all icons, labels, UI constants, and theme settings to allow easy re-theming.
Colors are predominantly handled by CSS variables in style.css, but Gradio theme overrides are here.
"""
import gradio as gr

class ICONS:
    HOME = "🏠"
    CHAT = "🤖"
    SUMMARIZE = "📝"
    IDEAS = "💡"
    PDF = "📄"
    VOICE = "🎤"
    DASHBOARD = "📊"
    SETTINGS = "⚙️"
    SEARCH = "🔍"
    NOTIFICATIONS = "🔔"
    THEME = "🌗"
    PROFILE = "👤"
    RESUME = "💼"
    IMAGE = "🖼️"
    CODE = "💻"
    EMAIL = "✉️"
    PRESENTATION = "📊"
    RESEARCH = "🔬"

class LABELS:
    APP_NAME = "AI Workspace Pro"
    APP_SUBTITLE = "Your Intelligent Productivity Hub powered by Gemini AI"
    VERSION = "v1.0.0"
    POWERED_BY = "Powered by Gemini AI"
    
    # Sidebar Sections
    CORE_FEATURES = "CORE FEATURES"
    UPCOMING = "UPCOMING"
    
    # Dashboard
    WHAT_TO_DO = "What would you like to do today?"
    RECENT_SESSIONS = "Recent Sessions"
    QUICK_TEMPLATES = "Quick Templates"
    TIP_OF_THE_DAY = "💡 Tip of the Day: Upload PDFs to summarize large documents quickly."

class UI_CLASSES:
    # Buttons
    BTN_PRIMARY = "btn-primary"
    BTN_SECONDARY = "btn-secondary"
    SIDEBAR_BTN = "sidebar-btn"
    SIDEBAR_BTN_ACTIVE = ["sidebar-btn", "active"]
    
    # Typography
    HEADING_XL = "heading-xl text-gradient"
    HEADING_LG = "heading-lg text-primary"
    HEADING_MD = "heading-md text-primary"
    TEXT_SUBTITLE = "text-body-lg text-secondary"
    
    # Containers
    GLASS_PANEL = "glass-panel"
    PREMIUM_CARD = "premium-card animate-fade-in"
    UNIVERSAL_INPUT = "universal-input"
    
    # Gradients
    GRAD_PURPLE = "grad-purple"
    GRAD_PINK = "grad-pink"
    GRAD_CYAN = "grad-cyan"
    GRAD_BLUE = "grad-blue"

def get_gradio_theme():
    """Returns the base Gradio theme configured to use our CSS variables."""
    return gr.themes.Default(
        primary_hue="indigo",
        secondary_hue="purple",
        neutral_hue="slate",
        font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"]
    ).set(
        body_background_fill="var(--bg-base)",
        body_background_fill_dark="var(--bg-base)",
        body_text_color="var(--text-primary)",
        body_text_color_dark="var(--text-primary)",
        background_fill_primary="var(--bg-card)",
        background_fill_primary_dark="var(--bg-card)",
        background_fill_secondary="var(--bg-sidebar)",
        background_fill_secondary_dark="var(--bg-sidebar)",
        border_color_primary="var(--border-color)",
        border_color_primary_dark="var(--border-color)",
        block_background_fill="transparent",
        block_background_fill_dark="transparent",
        block_border_width="0px"
    )
