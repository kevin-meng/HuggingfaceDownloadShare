import os 
import gradio as gr
import huggingface_hub as hh
from huggingface_hub import hf_hub_download
from bypy import ByPy


def format_size(bytes, precision=2):
    """
    Convert a file size in bytes to a human-readable format like KB, MB, GB, etc.
    Huggingface use 1000 not 1024
    """
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(bytes)
    index = 0

    while size >= 1000 and index < len(units) - 1:
        index += 1
        size /= 1000

    return f"{size:.{precision}f} {units[index]}"


def list_repo_files_info(repo_id,token=None):
    data_ls = [] 
    for file in list(hh.list_files_info(repo_id)):
        data_ls.append([file.path,format_size(file.size)])
    files = [file[0] for file in data_ls]
    filenames = gr.Dropdown(choices = files, label="选择文件",allow_custom_value=True,multiselect=True)
    return data_ls, filenames


def download_file(repo_id,filenames):
    print(filenames)
    repo_name = repo_id.replace("/","---")
    
    for filename in filenames:
        print(filename)
        out = hh.hf_hub_download(repo_id=repo_id,filename=filename,local_dir=f"/data/download/{repo_name}",local_dir_use_symlinks=False,force_download =True)
    out_path = f"/data/download/{repo_name}"
    return out_path



def upload_by_path(source_path,dest_path):
    bp = ByPy()
    out = bp.syncup(
      source_path,
      dest_path
    )
    # out = "test"
    
    return out

def upload_by_file(source_path):
    bp = ByPy()
    out = bp.upload(
      source_path,
      source_path.split("/")[-1]
    )
    # out = "test"
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
                repo = gr.Textbox(placeholder="输入 repo_id")
                list_bt = gr.Button("获取文件清单", variant="primary")
                
                filenames = gr.Dropdown(label="选择文件",allow_custom_value=False,multiselect=True)
                submit_bt = gr.Button("下载", variant="primary")
                gr.Markdown("下载路径：")
                output = gr.Markdown(label="对应路径")
                
            with gr.Column():
                output_df = gr.Dataframe(headers=['文件名', '文件大小'])
                        
            list_bt.click(list_repo_files_info, inputs=repo, outputs=[output_df,filenames])

            submit_bt.click(download_file, [repo, filenames], outputs=output)

        gr.Markdown("---")

        with gr.Row():
            bp = ByPy()
            key = bp.list()
            with gr.Column():
                gr.Markdown("### 输入上传百度云")
        with gr.Row():
            with gr.Column():
                submit_by = gr.Button("上传", variant="primary")
                result = gr.Markdown(label="结果路径")

            with gr.Column():
                pass
            submit_by.click(upload_by_file,output,outputs= result)

    return demo


if __name__ == "__main__":
    demo = app()
    demo.launch(share=True)



