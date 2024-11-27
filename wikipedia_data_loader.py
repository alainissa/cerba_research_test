import datetime
from wikipedia_api import WikipediaAPI

class WikipediaDataLoader:
    """
    A class for loading data from Wikipedia API into a database.
    """
    def __init__(self, database_connector):
        """
        Initializes the WikipediaDataLoader with a database connector.

        Args:
            database_connector (object): A WikipediaDatabase object that provides methods for inserting data into the database.
        """
        self.database = database_connector

    def load_data(self, recent_changes):
        """
        Loads recent changes and associated page data into the database.

        Args:
            recent_changes (list): A list of recent changes from Wikipedia API.
        """
        # A set to keep track of page IDs that have already been processed
        already_used_page_ids = set()

        for change in recent_changes:
            page_id = change["pageid"]
            self.database.insert_recent_change({
                "page_id": page_id,
                "title": change["title"],
                "timestamp": datetime.datetime.fromisoformat(change["timestamp"].replace("Z", "+00:00")),
                "user": change.get("user", "unknown")
            })
            # Check if the page data for this page ID has already been processed
            if page_id not in already_used_page_ids:
                page_content = WikipediaAPI.fetch_page_content(page_id)
                if isinstance(page_content, dict): #Noticed that when we fetch a list it is always because the page_id is missing.
                    page_data = page_content[str(page_id)]
                    self.database.insert_page_data({
                        "pageid": page_id,
                        "ns": page_data.get('ns'),
                        "title": page_data.get('title'),
                        "touched": page_data.get('touched'),
                        "pagelanguage": page_data.get('pagelanguage'),
                        "contentmodel": page_data.get('contentmodel'),
                        "pagelanguagehtmlcode": page_data.get('pagelanguagehtmlcode'),
                        "lastrevid": page_data.get('lastrevid'),
                        "length": page_data.get('length')
                    })
                    already_used_page_ids.add(page_id) #We add this id in order to avoid adding twice the same ID (the database will raise an error otherwise)