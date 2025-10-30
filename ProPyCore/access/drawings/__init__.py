from .sets import Sets
from .revisions import Revisions
from .uploads import Uploads
from .tiles import Tiles


class Drawings:
    def __init__(self, access_token, server_url):
        self.sets = Sets(access_token, server_url)
        self.revisions = Revisions(access_token, server_url)
        self.uploads = Uploads(access_token, server_url)
        self.tiles = Tiles(access_token, server_url)