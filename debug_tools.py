import sys
import os

# Add the current directory to sys.path so we can import card_services_agent
sys.path.append(os.getcwd())

try:
    from card_services_agent.tools import card_ops
    print(f"Data cache type: {type(card_ops._DATA_CACHE)}")
    print(f"Data cache content: {card_ops._DATA_CACHE}")
    
    result = card_ops.approve_card()
    print(f"Approve card result: {result}")
except Exception as e:
    print(f"Error: {e}")
