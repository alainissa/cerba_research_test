import requests

class WikipediaAPI:
    """
    A class that will fetch data from Wikipedia using the Wikipedia API.
    """

    BASE_URL = "https://en.wikipedia.org/w/api.php"     # Base URL for Wikimedia API requests

    @staticmethod
    def fetch_recent_changes(date):
        """
            Fetches a list of recent changes made on Wikipedia starting from a specified date.

            Args:
                date (str): The start date for fetching changes in ISO 8601 format (YYYY-MM-DD).

            Returns:
                list: A list of recent changes, including details like title, IDs, sizes, user, and timestamp.
        """
        params = {
            "format": "json",
            "rcprop": "title|ids|sizes|flags|user|timestamp|changes",
            "rcstart": f"{date}T00:00:00Z",
            "list": "recentchanges",
            "action": "query",
            "rclimit": "max" # the maximum being 500 because of limitation
        }
        response = requests.get(WikipediaAPI.BASE_URL, params=params)
        response.raise_for_status() # Raise an error if the request failed
        data = response.json()
        return data['query']['recentchanges']

    @staticmethod
    def fetch_page_content(page_id):
        """
        Fetches metadata and content-related information for a given Wikipedia page.

        Args:
            page_id (int): The ID of the Wikipedia page.

        Returns:
            dict: A dictionary containing metadata and details about the specified page.
        """
        params = {
            "action": "query",
            "prop": "info",
            "pageids": page_id,
            "format": "json"
        }
        response = requests.get(WikipediaAPI.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data['query']['pages']