# Restaurant Management System

A comprehensive restaurant management system with backend, frontend, mobile app, and database components.

## Project Structure

```
.
├── backend/           # Django REST API
├── frontend/         # React web application
├── mobile/          # React Native mobile app
└── database/        # Database queries and schema
```

## Project Task Mapping

| Section/Task         | File(s) / Location                                      | Description                                      |
|----------------------|---------------------------------------------------------|--------------------------------------------------|
| Backend Model/API    | `backend/restaurants/models.py`, `serializers.py`, `views.py`, `urls.py` | Django model, serializer, API, and routing       |
| Data Processing      | `backend/restaurants/utils.py`                          | Total revenue calculation function               |
| React List           | `frontend/src/components/RestaurantList.tsx`            | Fetch and display restaurants                    |
| React Form           | `frontend/src/components/RestaurantForm.tsx`            | Add restaurant form with validation              |
| Mobile List          | `mobile/screens/RestaurantListScreen.js` (or similar)   | Mobile app restaurant list screen                |
| SQL Query            | `database/sql/top_restaurants.sql`                      | Top 5 restaurants SQL query                      |
| MQTT                 | `backend/restaurants/mqtt_client.py`                    | MQTT publisher/subscriber                        |
| gRPC                 | `backend/restaurants/proto/restaurant.proto`, `grpc_server.py`, `grpc_client.py` | gRPC service, server, and client                 |
| Redis Caching        | `backend/restaurants/cache.py`                          | Redis caching logic                              |

## Features

### Backend (Django)
- RESTful API for restaurant management
- MQTT integration for real-time updates
- gRPC service for efficient communication
- Redis caching for improved performance

### Frontend (React)
- Modern UI with Material-UI components
- Restaurant listing and details
- Form for adding new restaurants
- Real-time updates

### Mobile (React Native)
- Native mobile experience
- Restaurant listing and details
- Clean and responsive design

### Database (PostgreSQL)
- Optimized queries
- Proper indexing
- Efficient data retrieval

## Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### Mobile
```bash
cd mobile
npm install
npm start
```

### Database
```bash
cd database
psql -d your_database_name -f sql/top_restaurants.sql
```

## API Documentation

### REST API Endpoints
- `GET /api/restaurants/` - List all restaurants
- `POST /api/restaurants/` - Create a new restaurant
- `GET /api/restaurants/{id}/` - Get restaurant details
- `PUT /api/restaurants/{id}/` - Update restaurant
- `DELETE /api/restaurants/{id}/` - Delete restaurant

### gRPC Service
- `GetRestaurant` - Get restaurant details by ID

### MQTT Topics
- `restaurant/orders` - Real-time order updates

## Development

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL
- Redis
- MQTT Broker

### Environment Variables
Create a `.env` file in the backend directory:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0
MQTT_BROKER=localhost
MQTT_PORT=1883
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 