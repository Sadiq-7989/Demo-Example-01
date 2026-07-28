import gradio as gr
from utils.theme import UI_CLASSES, LABELS, ICONS

def create_home_view():
    with gr.Column(visible=False, elem_classes="page-content") as view:
        # Hero Banner
        with gr.Column(elem_classes="hero-banner"):
            gr.Markdown(f"# {LABELS.APP_NAME}", elem_classes="heading-xl")
            gr.Markdown(f"**Welcome back!** {LABELS.APP_SUBTITLE}", elem_classes="text-body-lg text-primary")
            
        # Analytics / Top Metrics
        with gr.Row():
            # Chats Metric
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_PURPLE):
                gr.Markdown(f"### {ICONS.CHAT} AI Chats")
                gr.Markdown("## 124", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                    <span class="status-badge" style="font-size: 0.7rem;">▲ +15 Today</span>
                    <div style="width: 50%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px;">
                        <div style="width: 75%; height: 100%; background: var(--accent-primary); border-radius: 2px;"></div>
                    </div>
                </div>
                """)
            
            # PDFs Metric
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_PINK):
                gr.Markdown(f"### {ICONS.PDF} PDFs Analyzed")
                gr.Markdown("## 56", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                    <span class="status-badge" style="font-size: 0.7rem;">▲ +4 Today</span>
                    <div style="width: 50%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px;">
                        <div style="width: 40%; height: 100%; background: var(--accent-secondary); border-radius: 2px;"></div>
                    </div>
                </div>
                """)
                
            # Voice Metric
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_CYAN):
                gr.Markdown(f"### {ICONS.VOICE} Voice Sessions")
                gr.Markdown("## 17", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                    <span class="status-badge" style="font-size: 0.7rem;">▲ +2 Today</span>
                    <div style="width: 50%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px;">
                        <div style="width: 60%; height: 100%; background: var(--accent-tertiary); border-radius: 2px;"></div>
                    </div>
                </div>
                """)

        gr.HTML("<div style='height: 2rem;'></div>")

        # Main Layout: Two Columns (Left: Quick Actions + Templates, Right: Recent Sessions + Tip)
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown(f"### {LABELS.QUICK_TEMPLATES}", elem_classes="heading-md")
                
                with gr.Row():
                    btn_resume = gr.Button(f"{ICONS.RESUME} Resume", elem_classes=UI_CLASSES.BTN_SECONDARY)
                    btn_email = gr.Button(f"{ICONS.EMAIL} Email", elem_classes=UI_CLASSES.BTN_SECONDARY)
                    btn_presentation = gr.Button(f"{ICONS.PRESENTATION} Slides", elem_classes=UI_CLASSES.BTN_SECONDARY)
                with gr.Row():
                    btn_research = gr.Button(f"{ICONS.RESEARCH} Research", elem_classes=UI_CLASSES.BTN_SECONDARY)
                    btn_blog = gr.Button(f"📝 Blog Post", elem_classes=UI_CLASSES.BTN_SECONDARY)
                    btn_assignment = gr.Button(f"🎓 Assignment", elem_classes=UI_CLASSES.BTN_SECONDARY)
                    
            with gr.Column(scale=1):
                # Tip of the day
                with gr.Column(elem_classes=[UI_CLASSES.GLASS_PANEL, "tip-panel"]):
                    gr.Markdown(LABELS.TIP_OF_THE_DAY, elem_classes="text-body text-primary")
                
                # Recent Sessions
                gr.Markdown(f"### {LABELS.RECENT_SESSIONS}", elem_classes="heading-md")
                gr.HTML("""
                <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                    <div class="glass-panel" style="padding: 1rem; display: flex; align-items: center; gap: 1rem;">
                        <div style="font-size: 1.5rem;">🤖</div>
                        <div style="flex-grow: 1;">
                            <div style="font-weight: 500;">Project Planning Chat</div>
                            <div style="font-size: 0.75rem; color: var(--text-secondary);">2 mins ago</div>
                        </div>
                        <div class="status-badge">Completed</div>
                    </div>
                    <div class="glass-panel" style="padding: 1rem; display: flex; align-items: center; gap: 1rem;">
                        <div style="font-size: 1.5rem;">📄</div>
                        <div style="flex-grow: 1;">
                            <div style="font-weight: 500;">Q3_Financial_Report.pdf</div>
                            <div style="font-size: 0.75rem; color: var(--text-secondary);">1 hour ago</div>
                        </div>
                        <div class="status-badge" style="background: rgba(59, 130, 246, 0.1); color: var(--accent-quaternary); border-color: rgba(59, 130, 246, 0.2);">Summarized</div>
                    </div>
                    <div class="glass-panel" style="padding: 1rem; display: flex; align-items: center; gap: 1rem;">
                        <div style="font-size: 1.5rem;">💡</div>
                        <div style="flex-grow: 1;">
                            <div style="font-weight: 500;">Marketing Campaign Ideas</div>
                            <div style="font-size: 0.75rem; color: var(--text-secondary);">Yesterday</div>
                        </div>
                        <div class="status-badge" style="background: rgba(139, 92, 246, 0.1); color: var(--accent-primary); border-color: rgba(139, 92, 246, 0.2);">Generated</div>
                    </div>
                </div>
                """)
                
    return view
