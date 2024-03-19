from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import DeliveryOut, DeliveryIn, DeliveryUpdate
from app.api import db_manager
from app.api.service import is_restaurant_present

delivery = APIRouter()

@delivery.post('/', response_model=DeliveryIn, status_code=201)
async def create_Delivery(payload: DeliveryIn):
    for restaurant_id in payload.restaurants_id:
        if not is_restaurant_present(restaurant_id):
            raise HTTPException(status_code=404, detail=f"Restaurant with given id:{restaurant_id} not found")

    delivery_id = await db_manager.add_delivery(payload)
    response = {
        'id': delivery_id,
        **payload.dict()
    }

    return response

@delivery.get('/', response_model=List[DeliveryOut])
async def get_deliveries():
    return await db_manager.get_all_deliveries()

@delivery.get('/{id}/', response_model=DeliveryOut)
async def get_delivery(id: int):
    delivery = await db_manager.get_delivery(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return delivery

@delivery.put('/{id}/', response_model=DeliveryOut)
async def update_delivery(id: int, payload: DeliveryUpdate):
    delivery = await db_manager.get_delivery(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")

    update_data = payload.dict(exclude_unset=True)

    if 'restaurants_id' in update_data:
        for restaurant_id in payload.restaurants_id:
            if not is_restaurant_present(restaurant_id):
                raise HTTPException(status_code=404, detail=f"Restaurant with given id:{restaurant_id} not found")

    delivery_in_db = DeliveryIn(**delivery)

    updated_delivery = delivery_in_db.copy(update=update_data)

    return await db_manager.update_delivery(id, updated_delivery)

@delivery.delete('/{id}/', response_model=None)
async def delete_delivery(id: int):
    delivery = await db_manager.get_delivery(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return await db_manager.delete_delivery(id)