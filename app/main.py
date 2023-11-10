from fastapi import FastAPI, Path, Request, status
from typing import Any, Callable, TypeVar
from contexts import *
from models import *
from dtomodels import *


T = TypeVar('T')
context = PlayerContext()
app = FastAPI()


def first(src: list[T], cond: Callable[[T], bool]) -> T | None:
    for obj in src:
        if cond(obj):
            return obj

    return None


@app.get('/players/{player_id}')
async def get_players(player_id: int):
    try_find = first(context.Players, lambda player: player.id == player_id)
    if (try_find):
        return try_find

    return "OOps"


@app.post('/players/add')
async def add_player(player: DtoPlayer):
    context.Players.append(PlayerModel(
        context.last_id + 1, player.name, player.price, player.desc))
    context.last_id += 1

    return status.HTTP_201_CREATED
