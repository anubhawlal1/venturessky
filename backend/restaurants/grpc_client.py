import grpc
import restaurant_pb2
import restaurant_pb2_grpc

class RestaurantClient:
    def __init__(self, host: str = 'localhost', port: int = 50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = restaurant_pb2_grpc.RestaurantServiceStub(self.channel)

    def get_restaurant(self, restaurant_id: int) -> dict:
        """
        Get restaurant details by ID using gRPC.
        
        Args:
            restaurant_id: The ID of the restaurant to retrieve
            
        Returns:
            dict: Restaurant details or None if not found
        """
        try:
            request = restaurant_pb2.RestaurantRequest(restaurant_id=restaurant_id)
            response = self.stub.GetRestaurant(request)
            
            return {
                'id': response.id,
                'name': response.name,
                'address': response.address,
                'phone_number': response.phone_number,
                'rating': response.rating
            }
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                print(f"Restaurant with ID {restaurant_id} not found")
            else:
                print(f"Error getting restaurant: {e.details()}")
            return None

# Example usage
if __name__ == '__main__':
    client = RestaurantClient()
    
    # Get restaurant with ID 1
    restaurant = client.get_restaurant(1)
    
    if restaurant:
        print("Restaurant details:")
        print(f"Name: {restaurant['name']}")
        print(f"Address: {restaurant['address']}")
        print(f"Phone: {restaurant['phone_number']}")
        print(f"Rating: {restaurant['rating']}") 