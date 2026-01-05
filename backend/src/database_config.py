from databases import Database

from settings import settings

# PostgreSQL Database connection
database = Database(str(settings.database_url))
