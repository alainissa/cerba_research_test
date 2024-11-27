from wikipedia_api import WikipediaAPI
from wikipedia_data_loader import WikipediaDataLoader
from wikipedia_database import WikipediaDatabase

if __name__ == "__main__":
    database_url = "postgresql://postgres:postgres@localhost:5432/wikipedia" #the database URL
    database = WikipediaDatabase(database_url) #A link to the database methods

    print('Fetching recent changes from Wikipedia')
    recent_changes = WikipediaAPI.fetch_recent_changes("2024-10-31")

    print('Loading data into database')
    loader = WikipediaDataLoader(database)
    loader.load_data(recent_changes)
    print('Done')