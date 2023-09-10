# 使用 Python 3.9 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 克隆 GitHub 存储库的内容
RUN git clone https://github.com/kevin-meng/HuggingfaceDownloadShare.git

# 切换到克隆的存储库目录
WORKDIR /app/HuggingfaceDownloadShare

# 安装依赖项
RUN pip install -r requirements.txt

# 指定容器启动命令（示例中为一个占位的命令，你可以根据你的需求修改）
CMD ["python", "app.py"]
