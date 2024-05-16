#!/usr/bin/python3

import os

dynatrace_secret_api_key = os.environ['dynatrace_api_key']

print(f'My dynatrace api secret is *** {dynatrace_secret_api_key} ***')