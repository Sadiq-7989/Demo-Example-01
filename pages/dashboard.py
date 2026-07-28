import gradio as gr
from utils.theme import UI_CLASSES, ICONS

def create_dashboard_view():
    with gr.Column(visible=False, elem_classes="page-content") as view:
        gr.Markdown(f"# {ICONS.DASHBOARD} Analytics Dashboard", elem_classes=UI_CLASSES.HEADING_LG)
        gr.Markdown("Deep dive into your productivity and usage metrics.", elem_classes=UI_CLASSES.TEXT_SUBTITLE)
        
        with gr.Row():
            # Detailed Analytics Cards
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_PURPLE):
                gr.Markdown(f"### Total Queries")
                gr.Markdown("## 2,451", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                    <span class="status-badge">▲ 12% Weekly</span>
                    <span style="font-size: 0.8rem; color: var(--text-secondary);">Top Topic: Coding</span>
                </div>
                """)
            
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_PINK):
                gr.Markdown(f"### Time Saved")
                gr.Markdown("## 48 hrs", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                    <span class="status-badge">▲ 5% Weekly</span>
                    <span style="font-size: 0.8rem; color: var(--text-secondary);">Est. Value: $2.4k</span>
                </div>
                """)
                
            with gr.Column(elem_classes=UI_CLASSES.PREMIUM_CARD + " " + UI_CLASSES.GRAD_BLUE):
                gr.Markdown(f"### Storage Used")
                gr.Markdown("## 1.2 GB", elem_classes="text-primary")
                gr.HTML("""
                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                    <span class="status-badge" style="background: rgba(245, 158, 11, 0.1); color: var(--accent-warning); border-color: rgba(245, 158, 11, 0.2);">Warning: 80% Full</span>
                </div>
                <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; margin-top: 0.5rem;">
                    <div style="width: 80%; height: 100%; background: var(--accent-warning); border-radius: 3px;"></div>
                </div>
                """)
                
        gr.HTML("<div style='height: 2rem;'></div>")
        
        with gr.Row():
            with gr.Column(scale=2, elem_classes=[UI_CLASSES.GLASS_PANEL, "pad-8"]):
                gr.Markdown("### Usage Over Time (Placeholder Chart)")
                # UI Only Placeholder for Chart
                gr.HTML("""
                <div style="width: 100%; height: 300px; display: flex; align-items: flex-end; gap: 1rem; padding-top: 2rem; border-bottom: 1px solid var(--border-color);">
                    <div style="flex-grow: 1; height: 40%; background: linear-gradient(to top, var(--accent-primary), transparent); border-radius: 4px 4px 0 0;"></div>
                    <div style="flex-grow: 1; height: 60%; background: linear-gradient(to top, var(--accent-secondary), transparent); border-radius: 4px 4px 0 0;"></div>
                    <div style="flex-grow: 1; height: 85%; background: linear-gradient(to top, var(--accent-tertiary), transparent); border-radius: 4px 4px 0 0;"></div>
                    <div style="flex-grow: 1; height: 50%; background: linear-gradient(to top, var(--accent-primary), transparent); border-radius: 4px 4px 0 0;"></div>
                    <div style="flex-grow: 1; height: 95%; background: linear-gradient(to top, var(--accent-secondary), transparent); border-radius: 4px 4px 0 0;"></div>
                    <div style="flex-grow: 1; height: 75%; background: linear-gradient(to top, var(--accent-tertiary), transparent); border-radius: 4px 4px 0 0;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; color: var(--text-secondary); font-size: 0.8rem;">
                    <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span>
                </div>
                """)
                
            with gr.Column(scale=1, elem_classes=[UI_CLASSES.GLASS_PANEL, "pad-8"]):
                gr.Markdown("### Active Modules")
                gr.HTML("""
                <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
                    <li style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
                        <span>Chat AI</span> <span style="font-weight: bold; color: var(--accent-primary);">65%</span>
                    </li>
                    <li style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
                        <span>PDF Analyzer</span> <span style="font-weight: bold; color: var(--accent-secondary);">20%</span>
                    </li>
                    <li style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
                        <span>Idea Generator</span> <span style="font-weight: bold; color: var(--accent-tertiary);">10%</span>
                    </li>
                    <li style="display: flex; justify-content: space-between; align-items: center;">
                        <span>Voice Assistant</span> <span style="font-weight: bold; color: var(--accent-success);">5%</span>
                    </li>
                </ul>
                """)

    return view
