# OniDev's Helper Para Envio de Notificações

Envia notificações via bot do Telegram.

A documentação completa do pacote está disponível em: [https://onimusic.github.io/oni_notifications_helper/](https://onimusic.github.io/oni_notifications_helper/).

Para atualizar a documentação:
- Instale o Sphinx e o Sphinx-napoleon: `pip install Sphinx sphinxcontrib-napoleon`.
- Rode o napoleon no diretório base para compilar as docstrings escritas no padrão do Google para o Sphinx (por padrão, o Sphinx só consegue ler docstrings escritas em Re-Structured Text): `sphinx-apidoc -f -o docsrc/source .`.
- No diretório `docsrc/`, rode o comando `make github`. Isso vai gerar os arquivos html e static e enviá-los para a pasta docs, de onde o GitHub Pages puxa para postar no site.