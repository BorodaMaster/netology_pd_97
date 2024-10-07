import asyncio
import aiohttp
import more_itertools
import requests

from models import SessionDB, SwapiPeople, init_orm

URL = "https://swapi.dev/api/people"
MAX_REQUESTS = 10


def get_count_people():
    all_people = requests.get(URL)
    count = all_people.json().get('count')

    return count


async def get_people(people_id, session):
    response = await session.get(f"{URL}/{people_id}/")
    json_data = await response.json()

    return json_data


async def insert_people(people_list):
    async with SessionDB() as session:
        orm_model_list = [SwapiPeople(json=person_dict) for person_dict in people_list]
        session.add_all(orm_model_list)
        await session.commit()


async def main():
    await init_orm()

    count = get_count_people()

    async with aiohttp.ClientSession() as session_http:
        coros = (get_people(i, session_http) for i in range(1, count + 3))
        for coros_chunk in more_itertools.chunked(coros, MAX_REQUESTS):
            people_list = await asyncio.gather(*coros_chunk)
            asyncio.create_task(insert_people(people_list))

        tasks = asyncio.all_tasks()
        main_task = asyncio.current_task()
        tasks.remove(main_task)
        await asyncio.gather(*tasks)


asyncio.run(main())
