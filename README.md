# Alcatel SMS Read & Delete Tool
This script can read, delete individual SMS, or delete it all at once.

## Features
- Read SMS messages per contact.
- Delete individual messages.
- Delete all SMS messages from all contacts.
- Quick exit with q from any menu.

## Requirements
- Python 3
- `requests` library (install with `apt install python3-requests`)

## Installation
Download the python script:
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_read_delete_sms.py
```

## Usage
Run the script with:
```sh
python alcatel_read_delete_sms.py
```

## Configuration
Modify the `URL` variable in the script if your device has a different API endpoint.

## Network status check and simple storage checker
In addition to the SMS Reand and Delete script, I've also created a script to monitor the network status of your Alcatel device and another one to rapidly check if you have new messages.  
You can download and use it with the following command:
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_network_check.py
```
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_sms_checker.py
```

## Related Projects
If you are looking for a script that sends SMS using the same Alcatel IK40V modem, check out [IK40V_SMS](https://github.com/rmappleby/IK40V_SMS).

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to improve this project.

![alcatel_ik40v_read_delete](https://github.com/user-attachments/assets/4480953c-98f9-4ab0-ac68-20acdb83591e)

---

Made with 💪 for Alcatel device users.
