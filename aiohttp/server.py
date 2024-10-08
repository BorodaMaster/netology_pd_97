import json
import logging

from aiohttp import web

from models import Advertisement, SessionDB, init_orm, engine
from sqlalchemy.ext.asyncio import AsyncSession

app = web.Application()


async def orm_context(app):
    print("START SERVER...")
    await init_orm()
    yield
    await engine.dispose()
    print("STOP SERVER...")


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with SessionDB() as session:
        request.session = session
        response = await handler(request)
        return response


app.cleanup_ctx.append(orm_context)
app.middlewares.append(session_middleware)


async def get_advtg(advtg_id: int, session: AsyncSession) -> Advertisement:
    advtg = await session.get(Advertisement, advtg_id)

    if advtg is None:
        raise web.HTTPNotFound(
            text=json.dumps({"error": "Advertisement not found"}),
            content_type="application/json"
        )

    return advtg


async def create_advtg(advtg: Advertisement, session: AsyncSession) -> Advertisement:
    session.add(advtg)
    await session.commit()

    return advtg


class AdvertisementView(web.View):

    @property
    def advtg_id(self):
        return int(self.request.match_info["advtg_id"])

    @property
    def session(self) -> AsyncSession:
        return self.request.session

    async def get(self):
        advtg = await get_advtg(self.advtg_id, self.session)
        return web.json_response(advtg.json)

    async def post(self):
        json_data = await self.request.json()
        advtg = Advertisement(**json_data)
        advtg = await create_advtg(advtg, self.session)

        return web.json_response({"id": advtg.id})

    async def patch(self):
        json_data = await self.request.json()
        advtg = await get_advtg(self.advtg_id, self.session)
        for field, value in json_data.items():
            setattr(advtg, field, value)
        advtg = await create_advtg(advtg, self.session)

        return web.json_response({"id": advtg.id})

    async def delete(self):
        advtg = await get_advtg(self.advtg_id, self.session)
        await self.session.delete(advtg)
        await self.session.commit()

        return web.json_response({"status": "deleted"})


app.add_routes([
    web.post("/", AdvertisementView),
    web.get("/{advtg_id:\d+}", AdvertisementView),
    web.patch("/{advtg_id:\d+}", AdvertisementView),
    web.delete("/{advtg_id:\d+}", AdvertisementView)
])

logging.basicConfig(level=logging.DEBUG)
web.run_app(app)
