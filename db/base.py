from core.config import DATABASE_URL, APPS_MODELS

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}

# Multiple connections
# tortoise_orm = {
#     "connections": {
#         "default": expand_db_url(db_url, True),
#         "second": expand_db_url(db_url_second, True),
#     },
#     "apps": {
#         "models": {"models": ["tests.models", "aerich.models"], "default_connection": "default"},
#         "models_second": {"models": ["tests.models_second"], "default_connection": "second", },
#     },
# }
