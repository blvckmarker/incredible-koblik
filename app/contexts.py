from app.models import *


class PlayerContext:
    Players: list[PlayerModel] = []
    last_id: int = -1
