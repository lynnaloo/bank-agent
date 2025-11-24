import importlib.util
import sys
import os

file_path = 'card_services_agent/tools/card_ops.py'
module_name = 'card_ops'

try:
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    print(f"Data cache: {module._DATA_CACHE}")
    print(f"Approve card result: {module.approve_card()}")
except Exception as e:
    print(f"Error: {e}")
