# Use a imagem base do Ubuntu 18.04
FROM ubuntu:22.04

# Atualiza o sistema e instala as dependências necessárias
# RUN apt-get update && apt-get install -y \
#     software-properties-common \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update && apt-get install -y \
#     python3.9 \
#     python3.9-venv \
#     python3.9-dev \
#     && apt-get install -y curl \
#     && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
#     && python3.9 get-pip.py \
#     && rm get-pip.py

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3 python3-pip libgl1 libglib2.0-0

# Define python3.9 como o python padrão
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Instala o Jupyter Notebook
RUN pip install jupyter
RUN pip install dubins

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do diretório atual para o diretório de trabalho no container
COPY . /app

# Exponha a porta 8888 para acessar o Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
