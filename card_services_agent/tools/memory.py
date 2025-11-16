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
    data = {
        "state": {     
            "customer_id": "",
            "first_name": "",
            "last_name": "",
            "account_type": "",
            "date_opened": "",
            "cards": []
        } 
    }
    data["state"].update(callback_context.state)