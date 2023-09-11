mkdir -p /etc/data
cd /etc/data
git clone https://github.com/kevin-meng/HuggingfaceDownloadShare.git
cd HuggingfaceDownloadShare

docker build -t mengkevin/gradio_hg .
docker run -it -v /etc/data:/app/data  mengkevin/gradio_hg