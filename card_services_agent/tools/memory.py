from datetime import datetime
import json
import os
from typing import Dict, Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State
from google.adk.tools import ToolContext

def _load_customer(callback_context: CallbackContext):
    """
    Sets up the initial state.
    Set this as a callback as before_agent_call of the root_agent.
    This gets called before the system instruction is contructed.

    Args:
        callback_context: The callback context.
    """    
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct path to profiles directory (up one level from tools)
    profiles_dir = os.path.join(os.path.dirname(current_dir), 'profiles')
    sample_file = os.path.join(profiles_dir, 'sample_customer.json')
    
    try:
        with open(sample_file, 'r') as f:
            customer_data = json.load(f)
            # Update the session state with the customer data
            callback_context.session.state.update(customer_data)
    except Exception as e:
        print(f"Error loading sample customer: {e}")
        # Fallback to empty state if file load fails
        data = {
            "customer_id": "",
            "first_name": "",
            "last_name": "",
            "account_type": "",
            "date_opened": "",
            "cards": []
        } 
        callback_context.session.state.update(data)