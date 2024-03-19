from fastapi import FastAPI, APIRouter

app = FastAPI(openapi_url="/api/v1/deliveries/openapi.json", docs_url="/api/v1/deliveries/docs")

deliveries_router = APIRouter()

deliveries = [
    {'deliveries_id': 1, 'name': 'Яндекс еда',
     'descrption': 'Крупнейший сервис быстрой доставки еды из ресторанров',
     'count_users': '30000000', 'city': 'Moscow'},
    {'deliveries_id': 2, 'name': 'Delivery club',
     'descrption': 'Мобильная и десктопная платформа для доставки еды',
     'count_users': '15000000', 'city': 'Tomsk'},
    {'deliveries_id': 3, 'name': 'Chibbis',
     'descrption': 'Один из трёх крупнейших агрегаторов доставок еды в России',
     'count_users': '10000000', 'city': 'Arhangelsk'}
]


@deliveries_router.get("/")
async def read_deliveries():
    return deliveries

@deliveries_router.get("/{deliveries_id}")
async def read_delivery(deliveries_id: int):
    for delivery in deliveries:
        if delivery['deliveries_id'] == deliveries_id:
            return delivery
    return None

app.include_router(deliveries_router, prefix='/api/v1/deliveries', tags=['deliveries'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)