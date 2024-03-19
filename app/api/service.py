import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/restaurants/'

def is_restaurant_present(restaurant_id: int):
    return True