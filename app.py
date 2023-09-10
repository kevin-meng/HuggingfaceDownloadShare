import gradio as gr
from huggingface_hub import snapshot_download
import bypy

def download(repo_id):
    out = snapshot_download(repo_id=repo_id)
    return out

def app():
    with gr.Blocks(
        css="""#chatbot {
            font-size: 14px;
            min-height: 300px;
        }"""
    ) as demo:
        gr.Markdown("# Huggingface Download 😀")
        with gr.Row():
            input = gr.Textbox(placeholder="输入 repo_id")
            output = gr.Textbox(label="路径")
            submit_bt = gr.Button("Run", variant="primary")
        
        submit_bt.click(download,input,outputs= output)


    return demo


if __name__ == "__main__":
    demo = app()
    demo.launch(share=True)

