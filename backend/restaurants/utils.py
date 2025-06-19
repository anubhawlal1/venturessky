from typing import List, Dict, Union

def calculate_total_revenue(orders: List[Dict[str, Union[str, int, float]]]) -> float:
    """
    Calculate total revenue from a list of orders.
    
    Args:
        orders: List of dictionaries containing order details
               Each order should have 'item_name', 'quantity', and 'price_per_item'
    
    Returns:
        float: Total revenue
        
    Raises:
        ValueError: If input is invalid
    """
    if not isinstance(orders, list):
        raise ValueError("Input must be a list")
    
    if not orders:
        return 0.0
    
    total_revenue = 0.0
    
    for order in orders:
        if not all(key in order for key in ['item_name', 'quantity', 'price_per_item']):
            raise ValueError("Each order must contain 'item_name', 'quantity', and 'price_per_item'")
        
        try:
            quantity = float(order['quantity'])
            price = float(order['price_per_item'])
            
            if quantity < 0 or price < 0:
                raise ValueError("Quantity and price must be non-negative")
                
            total_revenue += quantity * price
        except (ValueError, TypeError):
            raise ValueError("Quantity and price must be valid numbers")
    
    return round(total_revenue, 2) 