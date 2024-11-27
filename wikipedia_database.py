from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table

class WikipediaDatabase:
    """
    A class to manage the database operations for storing Wikipedia data.
    """
    def __init__(self, database_url):
        """
        Initializes the WikipediaDatabase with the given database URL.

        Args:
            database_url (str): The URL for the database connection.
        """
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self._define_tables()
        self._create_tables()

    def _define_tables(self):
        """
        Defines the table schemas for storing recent changes and page data.
        """
        self.recent_changes = Table(
            "recent_changes", self.metadata,
            Column("id", Integer, primary_key=True),
            Column("page_id", Integer),
            Column("title", String),
            Column("timestamp", DateTime),
            Column("user", String)
        )

        self.page = Table(
            "page", self.metadata,
            Column("pageid", Integer, primary_key=True),
            Column("ns", Integer),
            Column("title", String),
            Column("touched", DateTime),
            Column("pagelanguage", String),
            Column("contentmodel", String),
            Column("pagelanguagehtmlcode", String),
            Column("lastrevid", Integer),
            Column("length", Integer)
        )

    def _create_tables(self):
        """
        Creates the tables in the database if they do not already exist.
        """
        self.metadata.create_all(self.engine)

    def insert_recent_change(self, change_data):
        """
        Inserts a record into the 'recent_changes' table.

        Args:
            change_data (dict): A dictionary containing recent change data.
        """
        with self.engine.connect() as connection:
            connection.execute(self.recent_changes.insert().values(change_data))
            connection.commit()

    def insert_page_data(self, page_data):
        """
        Inserts a record into the 'page' table.

        Args:
            page_data (dict): A dictionary containing page data.
        """
        with self.engine.connect() as connection:
            connection.execute(self.page.insert().values(page_data))
            connection.commit()