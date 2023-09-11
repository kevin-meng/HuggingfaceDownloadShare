import os 
import gradio as gr
from huggingface_hub import snapshot_download
from bypy import ByPy


def download(repo_id):
    out = snapshot_download(repo_id=repo_id,cache_dir="/app/data/",force_download =True)
    path_name = repo_id.replace("/","---")
    # 移动文件
    os.system(f"mkdir -p /app/downloads/{path_name}")
    os.system(f"mv -rf {out}/* /app/downloads/{path_name}")
    out_path = f"/app/downloads/{path_name}"
    return out_path


def upload_by_path(source_path,dest_path):
    bp = ByPy()
    out = bp.syncup(
      source_path,
      path_name
    )
    return out

def upload_by_file(source_path):
    bp = ByPy()
    out = bp.upload(
      source_path,
      source_path.split("/")[-1]
    )
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
            with gr.Column():
                input = gr.Textbox(placeholder="输入 repo_id")
                submit_bt = gr.Button("下载", variant="primary")
            with gr.Column():
                output = gr.Textbox(label="路径")

            
            submit_bt.click(download,input,outputs= output)

        with gr.Row():
            bp = ByPy()
            key = bp.list()
            with gr.Column():
                gr.Markdown("### 输入上传百度云")
        with gr.Row():
            with gr.Column():
                submit_by = gr.Button("上传", variant="primary")
                result = gr.Textbox(placeholder="结果路径")

            with gr.Column():
                pass
            submit_by.click(upload_by_path,output,outputs= result)

    return demo


if __name__ == "__main__":
    demo = app()
    demo.launch(share=True)

