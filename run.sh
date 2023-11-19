
mkdir -p /etc/data
cd /etc/data
git clone https://github.com/kevin-meng/HuggingfaceDownloadShare.git
cd HuggingfaceDownloadShare
mkdir download

docker build -t mengkevin/gradio_hg .
docker run --rm -it -v .:/data mengkevin/gradio_hg
