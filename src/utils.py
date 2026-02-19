import json
import re
import datetime

def get_timestamp():
    return datetime.datetime.now().isoformat()

def parse_config(data):
    return json.loads(data)

def flatten(lst):
    return [item for sublist in lst for item in sublist]