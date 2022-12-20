<h1 align="center"> YouTube video downloader </h1>

<p align="center">
<img src="https://lh3.googleusercontent.com/3zkP2SYe7yYoKKe47bsNe44yTgb4Ukh__rBbwXwgkjNRe4PykGG409ozBxzxkrubV7zHKjfxq6y9ShogWtMBMPyB3jiNps91LoNH8A=s200" alt="RocketHelp logo"/>
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/rogerroth/youtube-video-downloader"/>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
</p>

## ▶️ Projeto

Esta aplicação visa permitir o download de vídeos do YouTube através de linha de comando (CLI).

Como a ideia é executar o código via terminal, alguns parâmetros podem ser passados:

- `--link` a URL do vídeo do YouTube.
- `--resolution` a resolução que deseja baixar o vídeo. 
- `--oauth`[^1] para vídeos com restrição de idade é necessário definir este parâmetro como `True`.

[^1]: parâmetro não obrigatório.

Durante o download do vídeo, será exibido uma barra de progresso, com informações de tamanho do vídeo.

## Tecnologias e Estrutura

- [`Python`](https://www.python.org) Python é uma linguagem de programação que permite trabalhar rapidamente e integrar sistemas de forma mais eficaz.
- [`pytube`](https://pytube.io/en/latest/) Biblioteca responsável por fazer o download de vídeos do YouTube.

## 📲 Executando o projeto

### ✔️ Pré-requisitos

Para conseguir seguir este README e rodar o projeto você pode precisar dos seguintes itens:
- Git para clonar o projeto e acessar as "branches". Você pode instalar [aqui](https://git-scm.com/downloads);
- Python para podermos executar o projeto. Você pode instalá-lo [aqui](https://www.python.org);

Se quiser testar as instalações, rodar os comandos abaixo separadamente deve mostrar as respectivas versões.

```bash
git --version
python --version
```

### 🐙 Clonando o projeto
Para ter acesso aos arquivos do projeto você pode clonar usando o seguinte comando:
```bash
git clone https://github.com/RogerRoth/youtube-video-downloader
```

### ▶️ Rodando o Projeto

Agora que já tem a pasta do projeto na sua máquina, dentro dela instale as dependências:
```bash
pip install -r .\requirements.txt
```

Então podemos rodar o projeto:
```bash
python video-downloader.py --link='https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0' --resolution='1080p'
```
Pronto, aguarde o download e você terá um vídeo para assistir quando estiver offline ;).

## License

[MIT](LICENSE.md)