# 使用 Python 3.11 镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /data

# COPY . .

# 安装依赖项
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

# 指定容器启动命令（示例中为一个占位的命令，你可以根据你的需求修改）
CMD ["python", "app.py"]
