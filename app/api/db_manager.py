from app.api.models import DeliveryIn, DeliveryOut, DeliveryUpdate
from app.api.db import deliveries, database


async def add_delivery(payload: DeliveryIn):
    query = deliveries.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_deliveries():
    query = deliveries.select()
    return await database.fetch_all(query=query)


async def get_delivery(id):
    query = deliveries.select(deliveries.c.id == id)
    return await database.fetch_one(query=query)


async def delete_delivery(id: int):
    query = deliveries.delete().where(deliveries.c.id == id)
    return await database.execute(query=query)


async def update_delivery(id: int, payload: DeliveryIn):
    query = (
        deliveries
        .update()
        .where(deliveries.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
