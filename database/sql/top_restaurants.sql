-- Query to find top 5 highest-rated restaurants
SELECT 
    id,
    name,
    address,
    phone_number,
    rating
FROM 
    restaurants
WHERE 
    rating IS NOT NULL
ORDER BY 
    rating DESC
LIMIT 5;

-- Index to optimize the query
CREATE INDEX IF NOT EXISTS idx_restaurants_rating ON restaurants(rating DESC); 