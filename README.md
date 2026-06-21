# FastAPI CRUD

Uma API RESTful desenvolvida com FastAPI para fins de estudo, utilizando SQLAlchemy para persistência de dados, Alembic para migrações e Pytest para testes automatizados.

## Tecnologias

* FastAPI
* SQLAlchemy(ORM)
* Pydantic(Schemas)
* Alembic(Migrations)
* Pytest
* UV


## Instalação

Instale as dependências:

```bash
uv sync
```

Crie um arquivo `.env` com os seguinte campo:
```bash
DATABASE_URL="sqlite:///database.db"
```

## Executando a Aplicação

Inicie o servidor de desenvolvimento:

```bash
uv run task run
```

## Banco de Dados

Aplicar as migrações:

```bash
uv run alembic upgrade head
```

Criar uma nova migração:

```bash
uv run alembic revision --autogenerate -m "<desc>"
```

## Testes

Executar todos os testes:

```bash
uv run task test
```
