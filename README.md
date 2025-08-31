# Alcatel SMS Read & Delete Tool
This script can read, delete individual SMS, or delete all at once.

## Features
- Read SMS messages per contact.
- Delete individual messages.
- Delete all SMS messages from all contacts.
- Quick exit with `q` from any menu.

## Requirements
- Python 3
- `requests` library (install with `apt install python3-requests`)

## Installation
Download the Python script:
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_read_delete_sms.py
```

## Usage
Run the script with:
```sh
python3 alcatel_read_delete_sms.py
```

You will see a menu like:

```
=== Menu ===
1. Read and delete single messages
2. Delete ALL messages from ALL contacts
Choose an option (or type q to 'exit'):
```

### How to delete individual SMS
- After selecting option `1` (Read and delete single messages), the script lists messages per contact.  
- To delete a single message, enter it in the following format:  
```
ContactId:SMSId
```
For example, to delete SMS ID `65539` from contact ID `2`:
```
2:65539
```
- Press **Enter** without typing anything to go back to the main menu.  
- Press **q** at any point to quit the script.

### How to delete all messages
- Select option `2` and type `deleteall` to confirm deletion of all SMS messages from all contacts.

## Configuration
Modify the `URL` variable in the script if your device has a different API endpoint.

## Network status check and simple storage checker
In addition to the SMS Read & Delete script, there are scripts to monitor your Alcatel device network and rapidly check if you have new messages.  
Download them with:
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_network_check.py
```
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_sms_checker.py
```

## Related Projects
For sending SMS using the Alcatel IK40V modem, see [IK40V_SMS](https://github.com/rmappleby/IK40V_SMS).  
Special acknowledgment to rmappleby, who was fundamental for this script: thanks to his guidance, I understood where to look in the API to develop this tool.

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to improve this project.

![alcatel_ik40v_read_delete](https://github.com/user-attachments/assets/4480953c-98f9-4ab0-ac68-20acdb83591e)

---

Made with 💪 for Alcatel device users.

