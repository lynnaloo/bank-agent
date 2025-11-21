import json
import os
import logging
import time
from typing import Dict, Any, Optional
from datetime import datetime

# Configure logging
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=getattr(logging, log_level, logging.INFO))
logger = logging.getLogger(__name__)

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

def approve_card() -> Dict[str, Any]:
    """
    Approves a credit card for a customer.
    
    Args:
        last_four_digits: The last four digits of the card to approve (optional).
        customer_id: The ID of the customer (optional).
        
    Returns:
        The updated customer record.
    """
    start_time = time.time()
    logger.info("Tool 'approve_card' started")
    
    customer_data = _get_sample_data()
    
    # If no data, return empty dict
    if not customer_data:
        logger.warning("Tool 'approve_card' found no data")
        return {}

    # Find and update the card
    customer_data["action"] = "Pending approval"
    customer_data["reason"] = ""
    if "cards" in customer_data:
        for card in customer_data["cards"]:
            card["is_approved"] = True
            card["is_cancelled"] = False
            card["change_date"] = datetime.now().strftime("%Y-%m-%d")
            break
    
    duration = time.time() - start_time
    logger.info(f"Tool 'approve_card' completed in {duration:.4f}s")
    return customer_data

def cancel_card() -> Dict[str, Any]:
    """
    Cancels a credit card for a customer.
    
    Args:
        last_four_digits: The last four digits of the card to cancel (optional).
        customer_id: The ID of the customer (optional).
        
    Returns:
        The updated customer record.
    """
    start_time = time.time()
    logger.info("Tool 'cancel_card' started")

    customer_data = _get_sample_data()
    
    # If no data, return empty dict
    if not customer_data:
        logger.warning("Tool 'cancel_card' found no data")
        return {}

    # Find and update the card
    card_found = False
    customer_data["action"] = "Successfully cancelled"
    customer_data["reason"] = "Stolen card"
    if "cards" in customer_data:
        for card in customer_data["cards"]:
            card["is_approved"] = False
            card["is_cancelled"] = True
            card["change_date"] = datetime.now().strftime("%Y-%m-%d")
            break
    
    duration = time.time() - start_time
    logger.info(f"Tool 'cancel_card' completed in {duration:.4f}s")
    return customer_data
