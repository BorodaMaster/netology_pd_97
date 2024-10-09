import asyncio
import aiohttp
import more_itertools

from models import SessionDB, SwapiPeople, init_orm

URL = "https://swapi.dev/api/people"
MAX_REQUESTS = 10

filter_key = {'name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year''gender', 'homeworld',
               'films', 'species', 'vehicles', 'starships'}


async def get_count_people(session):
    all_people = await session.get(URL)
    json_data = await all_people.json()

    return json_data


async def get_people(people_id, session):
    response = await session.get(f"{URL}/{people_id}/")
    json_data = await response.json()

    return json_data


async def insert_people(people_list):
    async with SessionDB() as session:
        orm_model_list = [SwapiPeople(**{key: person_dict[key] for key in person_dict.keys() & filter_key})
                          for person_dict in people_list]
        session.add_all(orm_model_list)
        await session.commit()


async def main():
    await init_orm()

    async with aiohttp.ClientSession() as session_http:
        list_people = await asyncio.gather(get_count_people(session_http))
        count = list_people[0].get('count')

        coros = (get_people(i, session_http) for i in range(1, 0 + 3))
        for coros_chunk in more_itertools.chunked(coros, MAX_REQUESTS):
            people_list = await asyncio.gather(*coros_chunk)
            asyncio.create_task(insert_people(people_list))

        tasks = asyncio.all_tasks()
        main_task = asyncio.current_task()
        tasks.remove(main_task)
        await asyncio.gather(*tasks)


asyncio.run(main())
