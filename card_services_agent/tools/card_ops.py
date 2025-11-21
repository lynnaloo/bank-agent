import json
import os
from typing import Dict, Any, Optional
from datetime import datetime

# Global cache to store customer data in memory
_DATA_CACHE = None

def _get_sample_data() -> Dict[str, Any]:
    """Helper to load sample data."""
    global _DATA_CACHE
    if _DATA_CACHE is not None:
        return _DATA_CACHE

    current_dir = os.path.dirname(os.path.abspath(__file__))
    profiles_dir = os.path.join(os.path.dirname(current_dir), 'profiles')
    sample_file = os.path.join(profiles_dir, 'sample_customer.json')
    
    try:
        with open(sample_file, 'r') as f:
            data = json.load(f)
            # Handle the structure seen in the file: {"state": [ {customer...} ]}
            if "state" in data and isinstance(data["state"], list) and len(data["state"]) > 0:
                _DATA_CACHE = data["state"][0]
            else:
                _DATA_CACHE = data
            return _DATA_CACHE
    except Exception as e:
        print(f"Error loading sample data: {e}")
        return {}

def approve_card(last_four_digits: str, customer_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Approves a credit card for a customer.
    
    Args:
        last_four_digits: The last four digits of the card to approve.
        customer_id: The ID of the customer (optional).
        
    Returns:
        The updated customer record.
    """
    customer_data = _get_sample_data()
    
    # If no data, return empty dict
    if not customer_data:
        return {}

    # Find and update the card
    customer_data["action"] = "Pending approval"
    customer_data["reason"] = ""
    if "cards" in customer_data:
        for card in customer_data["cards"]:
            # if card.get("last_four_digits") == last_four_digits:
                card["is_approved"] = True
                card["is_cancelled"] = False
                card["change_date"] = datetime.now().strftime("%Y-%m-%d")
                break
    
    return customer_data

def cancel_card(last_four_digits: str, customer_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Cancels a credit card for a customer.
    
    Args:
        last_four_digits: The last four digits of the card to cancel.
        customer_id: The ID of the customer (optional).
        
    Returns:
        The updated customer record.
    """
    customer_data = _get_sample_data()
    
    # If no data, return empty dict
    if not customer_data:
        return {}

    # Find and update the card
    card_found = False
    customer_data["action"] = "Successfully cancelled"
    customer_data["reason"] = "Stolen card"
    if "cards" in customer_data:
        for card in customer_data["cards"]:
            # if card.get("last_four_digits") == last_four_digits:
                card["is_approved"] = False
                card["is_cancelled"] = True
                card["change_date"] = datetime.now().strftime("%Y-%m-%d")
                break
    
    return customer_data
