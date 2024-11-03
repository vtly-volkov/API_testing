from api.base_session import BaseSession
from api.endpoints import Endpoints


class ApiController(BaseSession):
    def get_random_poem(self):
        """
        Fetches a random poem from the API.
        :return: A randomly selected poem from the available endpoints.
        """
        random_poem = self.get(Endpoints.RANDOM)
        return random_poem

    def get_poem_by_author(self, author_name: str):
        """
        :param author_name: The name of the author whose poems are to be retrieved.
        :return: A list of poems written by the specified author.
        """
        poems = self.get(f"{Endpoints.AUTHOR.url}/{author_name}")
        return poems

    def get_poem_by_title(self, title: str):
        """
        :param title: The title of the poem to be retrieved
        :return: A list of poems matching the given title
        """
        poems = self.get(f"{Endpoints.TITLE.url}/{title}")
        return poems