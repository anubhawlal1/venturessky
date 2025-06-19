import grpc
from concurrent import futures
import restaurant_pb2
import restaurant_pb2_grpc
from .models import Restaurant

class RestaurantServicer(restaurant_pb2_grpc.RestaurantServiceServicer):
    def GetRestaurant(self, request, context):
        try:
            restaurant = Restaurant.objects.get(id=request.restaurant_id)
            return restaurant_pb2.RestaurantResponse(
                id=restaurant.id,
                name=restaurant.name,
                address=restaurant.address,
                phone_number=restaurant.phone_number,
                rating=float(restaurant.rating)
            )
        except Restaurant.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Restaurant not found')
            return restaurant_pb2.RestaurantResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return restaurant_pb2.RestaurantResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServiceServicer_to_server(
        RestaurantServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve() 