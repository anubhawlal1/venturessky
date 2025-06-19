import redis
import json
from typing import Optional, Dict, Any
from .models import Restaurant

class RestaurantCache:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )
        self.cache_expiry = 3600  # 1 hour in seconds

    def get_restaurant(self, restaurant_id: int) -> Optional[Dict[str, Any]]:
        """
        Get restaurant details from cache or database.
        
        Args:
            restaurant_id: The ID of the restaurant to retrieve
            
        Returns:
            dict: Restaurant details or None if not found
        """
        # Try to get from cache first
        cached_data = self.redis_client.get(f'restaurant:{restaurant_id}')
        
        if cached_data:
            return json.loads(cached_data)
        
        # If not in cache, get from database
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'phone_number': restaurant.phone_number,
                'rating': float(restaurant.rating)
            }
            
            # Store in cache
            self.redis_client.setex(
                f'restaurant:{restaurant_id}',
                self.cache_expiry,
                json.dumps(restaurant_data)
            )
            
            return restaurant_data
        except Restaurant.DoesNotExist:
            return None
        except Exception as e:
            print(f"Error getting restaurant: {e}")
            return None

    def invalidate_restaurant(self, restaurant_id: int):
        """
        Remove restaurant from cache.
        
        Args:
            restaurant_id: The ID of the restaurant to remove from cache
        """
        self.redis_client.delete(f'restaurant:{restaurant_id}')

    def update_restaurant(self, restaurant_id: int, restaurant_data: Dict[str, Any]):
        """
        Update restaurant in cache.
        
        Args:
            restaurant_id: The ID of the restaurant to update
            restaurant_data: The new restaurant data
        """
        self.redis_client.setex(
            f'restaurant:{restaurant_id}',
            self.cache_expiry,
            json.dumps(restaurant_data)
        )

# Example usage
if __name__ == '__main__':
    cache = RestaurantCache()
    
    # Get restaurant with ID 1
    restaurant = cache.get_restaurant(1)
    
    if restaurant:
        print("Restaurant details:")
        print(f"Name: {restaurant['name']}")
        print(f"Address: {restaurant['address']}")
        print(f"Phone: {restaurant['phone_number']}")
        print(f"Rating: {restaurant['rating']}")
        
        # Update restaurant in cache
        restaurant['rating'] = 4.5
        cache.update_restaurant(1, restaurant)
        
        # Invalidate cache
        cache.invalidate_restaurant(1) 