# Sistema de Gestão de Plataforma Educacional

Sistema desenvolvido com base no curso da Udemy ministrado por **Gileno Alves Santa Cruz Filho** (Desenvolvedor e Professor).

## Sobre o Projeto

Este projeto é uma **plataforma educacional**, com funcionalidades para gerenciamento de **cursos, aulas e usuários**.

O conteúdo original foi apresentado utilizando **Python 3** e **Django 1.6**.  
Nesta versão, o sistema foi adaptado para:

- **Python 3.8**
- **Django 2.x**

Foram feitas diversas atualizações para garantir compatibilidade com versões mais recentes e boas práticas modernas.

## Funcionalidades

- Cadastro e gerenciamento de cursos
- Criação de aulas vinculadas aos cursos
- Gerenciamento de usuários e permissões
- Área administrativa para controle da plataforma

## Tecnologias Utilizadas

- Python 3.8
- Django 2.x
- SQLite (banco de dados padrão)

## Como Rodar o Projeto

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```
   python manage.py runserver
   ```

## Créditos

Curso ministrado por **Gileno Alves Santa Cruz Filho** na plataforma **Udemy**.
