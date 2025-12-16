FFA .finance - V2

SOBRE O PROJETO

O FFA .finance - V2 é a segunda versão em desenvolvimento de um sistema de gerenciamento financeiro para microempresas.
O projeto tem como objetivo auxiliar no controle financeiro, organização de transações e visualização de dados, trazendo melhorias em relação à versão anterior, como refatoração do código, melhorias de usabilidade e modernização da interface.

Esta versão está sendo desenvolvida com foco em boas práticas de desenvolvimento, organização do projeto e escalabilidade.

---

TECNOLOGIAS UTILIZADAS

* Python 3.14.4
* Django 5.2.6
* HTML, CSS e JavaScript
* Tailwind CSS
* Banco de dados: SQLite (padrão do Django)
* Outras bibliotecas:
  
  * django-tailwind
  * Outras dependências listadas no arquivo requirements.txt

---

PRÉ-REQUISITOS

Antes de iniciar, certifique-se de ter instalado:

* Python 3.8 ou superior
* Git
* Banco de dados SQLite (já incluso no Django)
  (Opcional: MySQL ou PostgreSQL)

---

INSTALAÇÃO E CONFIGURAÇÃO

1. Clone o repositório

git clone [https://github.com/ademacirfilho/ffa-finance-V2.git](https://github.com/ademacirfilho/ffa-finance-V2.git)
cd ffa-finance-V2

2. Crie e ative um ambiente virtual

Windows:
python -m venv venv
venv\Scripts\activate

Linux / macOS:
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências

pip install -r requirements.txt

4. Execute as migrações do banco de dados

python manage.py migrate

5. (Opcional) Crie um superusuário

python manage.py createsuperuser

6. Execute o servidor

python manage.py runserver

Acesse no navegador:
[http://localhost:8000](http://localhost:8000)

---

ESTRUTURA DO PROJETO

ffa-finance-V2/

manage.py                  Script principal do Django
requirements.txt           Dependências do projeto
.env.example               Modelo de variáveis de ambiente
.env                       Variáveis de ambiente (NÃO vai para o Git)
.gitignore                 Arquivos ignorados pelo Git
README.md                  Este arquivo

config/                    Configurações do projeto Django
finance/                   Aplicação principal de finanças
usuarios/                  Aplicação de usuários e autenticação
templates/                 Templates HTML
static/                    Arquivos estáticos (CSS, JS, imagens)

docs/                      Documentação
manual/                    Manual do usuário
index.html

---

FUNCIONALIDADES

* Autenticação de usuários (registro, login e logout)
* Dashboard financeiro
* Gerenciamento de transações financeiras
* Organização por categorias
* Painel administrativo do Django

---

DOCUMENTAÇÃO

Para instruções detalhadas sobre o uso do sistema, consulte o Manual do Usuário em:

docs/manual/index.html

---

AUTORES

Ademacir Filho – Desenvolvedor principal
Francisco Guilherme – Colaborador
Francisco Freitas – Colaborador

---

LICENÇA

Este projeto está sob a licença MIT.
Consulte o arquivo LICENSE para mais informações.
