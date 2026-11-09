## MongoDB credentials

Copy `.env.example` to `.env` and set a strong `MONGO_INITDB_ROOT_PASSWORD`
before starting MongoDB with Docker Compose. The local `.env` file is ignored
by Git; do not commit real credentials.