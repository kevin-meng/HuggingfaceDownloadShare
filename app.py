import gradio as gr
import bypy


def app():
    with gr.Blocks(
        css="""#chatbot {
            font-size: 14px;
            min-height: 300px;
        }"""
    ) as demo:
        gr.Markdown("# Huggingface Download")
        
    return demo


if __name__ == "__main__":
    demo = app()
    demo.launch(share=True)

