import asyncio
import json
import pandas as pd
import aiohttp
from understat import Understat


def understat_json(name, id):

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            player_shots = await understat.get_player_shots(
                id, {"season": "2019"})
            shots = json.dumps(player_shots)
            with open(f'jsonfiles/{name}.json', 'w') as json_file:
                json.dump(shots, json_file)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
