#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alcatel SMS Storage Checker
Copyright (c) 2024 Anthony Borriello

This script retrieves and analyzes the SMS storage status of an Alcatel device via its web API.
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

# Device URL
URL = "http://ik40.home/jrd/webapi"

# JSON request to get SMS storage status
JSON_REQUEST = {
    "jsonrpc": "2.0",
    "method": "GetSMSStorageState",  # API method to get SMS storage state
    "params": {},
    "id": "6.4"
}

# Required headers for authentication
HEADERS = {
    "Host": "ik40.home",
    "Origin": "http://ik40.home",
    "Referer": "http://ik40.home/default.html"
}

def analyze_sms_storage_state():
    # Send a POST request to the device
    r = requests.post(URL, json=JSON_REQUEST, headers=HEADERS)

    # Check for response errors
    if r.status_code != 200:
        print("Request error:", r.status_code)
        quit()

    # If the returned JSON contains an error, print it
    response_json = r.json()
    if "error" in response_json:
        print("Response error:", response_json["error"])
        quit()

    # Analyze SMS storage state
    storage_state = response_json.get("result", {})

    # Extract values for analysis
    max_count = storage_state.get("MaxCount", 0)
    used_count = storage_state.get("TUseCount", 0)
    left_count = storage_state.get("LeftCount", 0)
    unread_sms_count = storage_state.get("UnreadSMSCount", 0)
    unread_report = storage_state.get("UnreadReport", 0)

    print("SMS Storage Status:")
    print(f"Maximum SMS capacity: {max_count}")
    print(f"Stored SMS: {used_count}")
    print(f"Available SMS slots: {left_count}")
    print(f"Unread SMS: {unread_sms_count}")
    print(f"Unread report SMS: {unread_report}")

    # Logic to analyze data
    if unread_sms_count > 0:
        print(f"Warning: There are {unread_sms_count} unread SMS messages.")
    else:
        print("All SMS messages have been read.")

    if left_count == 0:
        print("Warning: SMS storage is full!")
    elif left_count < max_count * 0.1:
        print("Warning: SMS storage is almost full!")

    if used_count > max_count * 0.8:
        print("Warning: More than 80% of SMS storage is used!")

    if unread_report > 0:
        print(f"There are {unread_report} unread SMS reports.")

if __name__ == "__main__":
    analyze_sms_storage_state()
