import os
import sys
import json
import re
import math
import random
import datetime
import collections
import itertools
import functools
import pathlib
import logging
import threading
import os  # duplicate import — LINTING error line 15

def get_timestamp():
    return datetime.datetime.now().isoformat()

def parse_config(data):
    return json.loads(data)

def flatten(lst):
    return [item for sublist in lst for item in sublist]
