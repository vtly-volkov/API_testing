from enum import Enum

from settings import get_settings


settings = get_settings()


class Endpoints(Enum):
    RANDOM = "random"
    AUTHOR = "author"
    TITLE = "title"

    @property
    def url(self):
        return f"{settings.API_URL}/{self.value}"
