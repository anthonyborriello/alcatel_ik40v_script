# Alcatel SMS Storage Checker

This script retrieves and analyzes the SMS storage status of an Alcatel device via its web API.
Currently, it only checks for unread messages and reports and provides warnings if storage is almost full.

## Features
- Retrieves SMS storage details from the device.
- Displays the number of stored, unread, and available SMS slots.
- Warns when storage is almost full or completely used.
- Alerts if there are unread SMS messages or reports.

## Requirements
- Python 3
- `requests` library (install with `apt install python3-requests`)

## Installation
Download the python script:
```sh
wget https://raw.githubusercontent.com/anthonyborriello/alcatel_ik40v_script/main/alcatel_sms_chacker.py
```

## Usage
Run the script with:
```sh
python alcatel_sms_chacker.py
```

## Configuration
Modify the `URL` variable in the script if your device has a different API endpoint.

## Related Projects
If you are looking for a script that sends SMS using the same Alcatel IK40V modem, check out [IK40V_SMS](https://github.com/rmappleby/IK40V_SMS).

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to improve this project.

![alcatel_read](https://github.com/user-attachments/assets/60175020-9269-4c08-834b-b3941ae5486a)

---

Made with ❤️ for Alcatel device users.
