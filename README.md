# FFA .finance – V2

## Sobre o Projeto

O **FFA .finance – V2** é a segunda versão desenvolvida de um sistema de **gerenciamento financeiro para microempresas**.
O **FFA .finance** é um gerenciador de finanças microempresariais, desenvolvido como parte do Projeto Integrador do curso de **Informática para Internet** no **IFRN**. Este sistema foi idealizado para ajudar microempresários a organizarem e controlarem suas finanças de forma prática e eficiente, permitindo que eles mantenham uma visão clara da saúde financeira de seus negócios.

O projeto tem como objetivo auxiliar no **controle financeiro**, **organização de transações** e **visualização de dados**, trazendo melhorias em relação à versão anterior, como **refatoração do código**, **melhorias de usabilidade** e **modernização da interface**.

Esta versão está sendo desenvolvida com foco em **boas práticas de desenvolvimento**, **organização do projeto** e **escalabilidade**, como parte do **Projeto Integrador do curso de Informática para Internet – IFRN**.

---

## Tecnologias Utilizadas

* **Python 3.12.4**
* **Django 5.2.6**
* **HTML, CSS e JavaScript**
* **Tailwind CSS**
* **Banco de dados:** SQLite (padrão do Django)
* **Outras bibliotecas:**

  * django-tailwind
  * (demais dependências listadas no `requirements.txt`)

---

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

* Python **3.8 ou superior**
* Git
* Banco de dados **SQLite** (já incluso no Django)

> Opcional:
>
> * MySQL ou PostgreSQL (caso deseje alterar a configuração padrão)

---

## Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/ademacirfilho/ffa-finance-V2.git
cd ffa-finance-V2
```

### 2. Crie e ative um ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

Este comando irá instalar todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 5. (Opcional) Crie um superusuário

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor

```bash
python manage.py runserver
```

Acesse no navegador:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## Estrutura do Projeto

```
ffa-finance-V2/
│
├── manage.py            # Script principal do Django
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Este arquivo
│
├── config/              # Configurações do projeto Django
├── finance/             # Aplicação principal de finanças
├── usuarios/            # Aplicação de usuários e autenticação
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS, imagens)
│
├── docs/                # Documentação
│   ├── manual/          # Manual do usuário
│   │   ├── index.html
│   │   └── ...
```

---

## Funcionalidades

* Autenticação de usuários (registro, login e logout)
* Dashboard financeiro
* Gerenciamento de transações financeiras
* Organização por categorias
* Painel administrativo do Django

---

## Documentação

Para instruções detalhadas sobre o uso do sistema, consulte o **Manual do Usuário** disponível em:

📄 `docs/manual/index.html`

---

## Autores

* **Ademacir Filho** – Desenvolvedor principal
* **Francisco Guilherme** – Colaborador
* **Francisco Freitas** – Colaborador

---

## Licença

Este projeto está sob a licença **MIT**.

Consulte o arquivo `LICENSE` para mais informações.
