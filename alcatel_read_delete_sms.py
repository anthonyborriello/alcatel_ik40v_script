#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alcatel SMS Read & Delete Tool
Copyright (c) 2024 Anthony Borriello

This script allows reading and deleting SMS messages stored on an Alcatel IK40V
(or similar devices) via its JSON-RPC web API.

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
import sys

URL = "http://192.168.1.1/jrd/webapi"
HEADERS = {
    "Host": "192.168.1.1",
    "Origin": "http://192.168.1.1",
    "Referer": "http://192.168.1.1/default.html"
}

def safe_input(prompt=""):
    """Input wrapper that allows 'q' to quit the script."""
    val = input(prompt).strip()
    if val.lower() == "q":
        print("Quit requested by user (q).")
        sys.exit(0)
    return val

def get_sms_contacts():
    payload = {
        "jsonrpc": "2.0",
        "method": "GetSMSContactList",
        "params": {"Page": 1},
        "id": "1"
    }
    r = requests.post(URL, json=payload, headers=HEADERS, timeout=5)
    return r.json().get("result", {}).get("SMSContactList", [])

def get_sms_for_contact(contact_id):
    payload = {
        "jsonrpc": "2.0",
        "method": "GetSMSContentList",
        "params": {"Page": 1, "ContactId": contact_id},
        "id": "2"
    }
    r = requests.post(URL, json=payload, headers=HEADERS, timeout=5)
    return r.json().get("result", {}).get("SMSContentList", [])

def delete_sms(del_flag, contact_id, sms_id=None):
    payload = {
        "jsonrpc": "2.0",
        "method": "DeleteSMS",
        "params": {
            "DelFlag": del_flag,
            "ContactId": contact_id,
            "SMSId": sms_id if sms_id is not None else 0
        },
        "id": "3"
    }
    r = requests.post(URL, json=payload, headers=HEADERS, timeout=5)
    res = r.json()
    return "result" in res and "error" not in res

def view_and_delete_single():
    contacts = get_sms_contacts()
    if not contacts:
        print("No contacts found.")
        return

    contacts_map = {c.get("ContactId"): c.get("PhoneNumber") for c in contacts}
    all_messages = []

    for contact_id in contacts_map:
        messages = get_sms_for_contact(contact_id)
        for msg in messages:
            all_messages.append({
                "ContactId": contact_id,
                "PhoneNumber": contacts_map[contact_id],
                "SMSId": msg.get("SMSId"),
                "SMSType": msg.get("SMSType"),
                "SMSTime": msg.get("SMSTime"),
                "SMSContent": msg.get("SMSContent"),
            })

    if not all_messages:
        print("No messages found.")
        return

    for contact_id in contacts_map:
        msgs = [m for m in all_messages if m["ContactId"] == contact_id]
        if not msgs:
            continue

        number = contacts_map[contact_id]
        if isinstance(number, list) and len(number) > 0:
            number = number[0]

        print(f"\nContact: {number} (ContactId: {contact_id})")

        received = [m for m in msgs if m["SMSType"] == 0]
        sent = [m for m in msgs if m["SMSType"] == 2]

        print("\n  --- Received messages ---")
        if not received:
            print("  No received messages.")
        else:
            for m in received:
                print(f"  {m['SMSTime']} - ID {m['SMSId']} [INBOX] {m['SMSContent']!r}")

        print("\n  --- Sent messages ---")
        if not sent:
            print("  No sent messages.")
        else:
            for m in sent:
                print(f"  {m['SMSTime']} - ID {m['SMSId']} [SENT] {m['SMSContent']!r}")

        print("\n" + "-" * 68 + "\n")

    while True:
        cmd = safe_input("\nEnter message to delete (format ContactId:SMSId), or press Enter to go back: ")
        if cmd == "":
            print("")
            break
        if ':' not in cmd:
            print("Invalid format. Use ContactId:SMSId")
            continue
        try:
            contact_id, sms_id = map(int, cmd.split(":"))
        except ValueError:
            print("Invalid numbers.")
            continue

        if any(m for m in all_messages if m["ContactId"] == contact_id and m["SMSId"] == sms_id):
            if delete_sms(2, contact_id, sms_id):
                print(f"Message ID {sms_id} deleted successfully.")

                remaining = get_sms_for_contact(contact_id)
                if not remaining:
                    delete_sms(1, contact_id)
                    print(f"Contact {contact_id} removed (no messages left).")
            else:
                print("Error deleting message.")
        else:
            print("Message not found.")

def delete_all_sms():
    contacts = get_sms_contacts()
    if not contacts:
        print("No contacts found.")
        return

    confirm = safe_input(
        "\nWARNING: This will delete *all* SMS messages from all contacts!\n"
        "Type 'deleteall' to confirm: "
    ).lower()

    if confirm != "deleteall":
        print("Operation cancelled.")
        return

    for contact in contacts:
        contact_id = contact.get("ContactId")
        phone = contact.get("PhoneNumber")
        if isinstance(phone, list) and len(phone) > 0:
            phone = phone[0]
        success = delete_sms(1, contact_id)
        if success:
            print(f"All messages from {phone!r} (ContactId {contact_id}) deleted successfully.")
        else:
            print(f"Error deleting messages from {phone!r} (ContactId {contact_id}).")

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Read and delete single messages")
        print("2. Delete ALL messages from ALL contacts")
        choice = safe_input("Choose an option (or type q to 'exit'): ").lower()

        if choice == "1":
            view_and_delete_single()
        elif choice == "2":
            delete_all_sms()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
