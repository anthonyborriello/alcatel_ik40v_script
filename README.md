# Alcatel SMS Storage Checker

This script retrieves and analyzes the SMS storage status of an Alcatel device via its web API.

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

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to improve this project.

---

Made with ❤️ for Alcatel device users.
