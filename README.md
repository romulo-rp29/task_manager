# Task Manager

## Descrição
Uma aplicação web simples para gerenciamento de tarefas diárias. Desenvolvida com Django, esta aplicação permite aos usuários criar, visualizar, editar e excluir tarefas. Apenas usuários autenticados podem acessar e gerenciar suas tarefas, garantindo segurança e personalização.

---

## Funcionalidades

### Básicas
- **Criar Tarefa:** Permite criar uma nova tarefa com título, descrição, prazo e status de conclusão.
- **Listar Tarefas:** Exibe todas as tarefas do usuário, com filtros para tarefas pendentes e concluídas.
- **Editar Tarefa:** Permite modificar os detalhes de uma tarefa existente.
- **Excluir Tarefa:** Remove uma tarefa definitivamente.

### Extras
- **Autenticação de Usuário:** Apenas usuários autenticados podem acessar o sistema.
- **Proteção de Dados:** Cada usuário só pode acessar suas próprias tarefas.
- **Filtros:** Exibição de tarefas por status (pendentes ou concluídas).

---

## Requisitos

### Pré-requisitos
- Python 3.10+
- Django 4.0+
- Banco de Dados SQLite (ou outro configurado no `settings.py`)

### Instalação

1. **Clonar o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd task_manager
   ```

2. **Criar e ativar um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Criar um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

---

## Uso

### Acessar o Sistema
- Acesse o sistema no navegador em `http://127.0.0.1:8000/`.
- Realize login com suas credenciais ou crie uma nova conta.

### Gerenciamento de Tarefas
1. **Criar uma nova tarefa:** Acesse a página "Criar Tarefa" e preencha os detalhes.
2. **Listar tarefas:** Navegue até a página inicial para ver suas tarefas. Use os filtros para tarefas pendentes ou concluídas.
3. **Editar uma tarefa:** Clique em "Editar" ao lado da tarefa que deseja modificar.
4. **Excluir uma tarefa:** Clique em "Excluir" para remover a tarefa.

---

## Estrutura do Projeto

```
project_root/
|-- task_manager/       # Configurações principais do projeto
|-- tasks/              # App principal para gerenciamento de tarefas
|   |-- migrations/     # Arquivos de migração do banco de dados
|   |-- templates/      # Templates HTML do app
|   |-- views.py        # Lógica das views
|   |-- models.py       # Modelos de dados
|-- db.sqlite3          # Banco de dados SQLite
|-- manage.py           # Ferramenta de gerenciamento do Django
```

---

## Funcionalidades Técnicas

1. **Modelos:**
   - `Task`: Armazena as informações das tarefas.
   - Campos: `title`, `description`, `completed`, `created_at`, `due_date`, `user`.

2. **Views:**
   - Criar, listar, editar e excluir tarefas.
   - Protegidas com `@login_required` e filtros por usuário autenticado.

3. **Templates:**
   - Utilizam o sistema de templates do Django para renderizar páginas HTML.

4. **URLs:**
   - Configuradas no arquivo `urls.py` do app e do projeto.

5. **Autenticação:**
   - Login e logout com sistema nativo do Django.
   - Proteção de dados para evitar acesso não autorizado.

---

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações: `git checkout -b feature/nova-funcionalidade`.
3. Envie suas alterações: `git push origin feature/nova-funcionalidade`.
4. Abra um pull request para revisão.

---

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Contato
Para dúvidas ou sugestões, entre em contato pelo e-mail: [romulo.rp29@gmail.com](mailto:romulo.rp29@gmail.com).
