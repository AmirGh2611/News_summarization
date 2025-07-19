import gradio as gr
from api_config import ui

page = gr.Interface(
    fn=ui,
    inputs=[gr.Textbox(label="Search", lines=2, placeholder="write search here..."),
            gr.Dropdown(label="Search field", choices=("title", "description", "keywords", "main_text")),
            gr.CheckboxGroup(label="categories",
                             choices=("general", "science", "sports", "business", "health",
                                      "entertainment", "tech", "politics", "food", "travel")),
            gr.Dropdown(label="language", choices=("en", "fa")),
            gr.Slider(value=10, minimum=1, maximum=100, step=1)],
    outputs=[],
    title="World News Search Engine",
)
page.launch()
