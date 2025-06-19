# Database Management

This section contains database-related files and queries for the restaurant management system.

## SQL Queries

### Top 5 Highest-Rated Restaurants

The query in `sql/top_restaurants.sql` finds the top 5 highest-rated restaurants in the database. The query:

1. Selects all relevant restaurant information
2. Filters out restaurants with NULL ratings
3. Orders results by rating in descending order
4. Limits the result to 5 restaurants
5. Uses an index on the rating column for optimal performance

## Performance Optimization

- Created an index on the `rating` column to improve query performance
- Used `LIMIT` to restrict the result set size
- Added `WHERE` clause to filter out invalid data

## Database Schema

The `restaurants` table has the following structure:

```sql
CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    address TEXT NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    rating DECIMAL(3,1)
);
```

## Usage

To run the query:

```bash
psql -d your_database_name -f sql/top_restaurants.sql
```

Make sure to replace `your_database_name` with your actual database name. 