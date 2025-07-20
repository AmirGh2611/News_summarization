import gradio as gr
from api_config import ui

page = gr.Interface(
    fn=ui,
    inputs=[gr.Textbox(label="Search", lines=1, placeholder="write search here..."),
            gr.Dropdown(label="Search field", choices=("title", "description", "keywords")),
            gr.CheckboxGroup(label="categories",
                             choices=("general", "science", "sports", "business", "health",
                                      "entertainment", "tech", "politics", "food", "travel")),
            gr.Slider(label="news number", value=1, minimum=1, maximum=100, step=1)],
    outputs=gr.Dataframe(label="News Result", wrap=True),
    title="World News Search Engine",
)
page.launch()
