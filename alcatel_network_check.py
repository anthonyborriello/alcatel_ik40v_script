#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alcatel Network Status Checker  
Copyright (c) 2024 Anthony Borriello  

This script retrieves and displays the network status of an Alcatel device via its web API.  
Licensed under the MIT License.  

GitHub Repository: https://github.com/anthonyborriello/alcatel_ik40v_script  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

See the LICENSE file for more details.  
"""

import requests
import json

# Device URL
URL = "http://ik40.home/jrd/webapi"

# Required headers for authentication
HEADERS = {
    "Host": "ik40.home",
    "Origin": "http://ik40.home",
    "Referer": "http://ik40.home/default.html",
}

# JSON request to get the system status (which includes all parameters)
JSON_GETSYSTEMSTATUS_REQUEST = {
    "jsonrpc": "2.0",
    "method": "GetSystemStatus",
    "params": {},
    "id": "1"
}

def get_system_status():
    # Send a POST request to the device
    r = requests.post(URL, json=JSON_GETSYSTEMSTATUS_REQUEST, headers=HEADERS)

    # Check for response errors
    if r.status_code != 200:
        print("Request error:", r.status_code)
        return

    # If the returned JSON contains an error, print it
    response_json = r.json()
    if "error" in response_json:
        print("Response error:", response_json["error"])
        return

    # Print all response parameters
    print(json.dumps(response_json, indent=4))

if __name__ == "__main__":
    get_system_status()
