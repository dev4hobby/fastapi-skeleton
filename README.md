# FastAPI Skeleton

It's a fastapi template for quickly creating a skeleton for your project.

## Usage

edit your `.env` file and run this command on your terminal

### Build container

```bash
docker-compose up --build
```

> or using `make` by running `make build-container`

### DB Init

```bash
docker exec -it fastapi aerich upgrade
```

> if `migrations/models/*.sql` not exist, run `make db-init`

## Development Environment

dependencies are managed via `pip-compile`
please create new python virtualenv and install dependencies.

### Install dependencies

```bash
make dep-sync
```

### Update dependencies

if you wanna add new dependencies,
add them to `requirements*.in`  and run this command

```bash
make dep-update
```

### Lock dependencies

if you wanna lock dependencies,
run this command

```bash
make dep-lock
```

## What I Using these on my project

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://github.com/encode/uvicorn)
- [starlette](https://github.com/encode/starlette)
- [gunicorn](https://github.com/benoitc/gunicorn)
- [tortoise-orm](https://github.com/tortoise/tortoise-orm)
- [aerich](https://github.com/tortoise/aerich)
- [asyncpg](https://github.com/MagicStack/asyncpg)