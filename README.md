# Bank Security Control Panel

## Description

Bank security control panel is a Django-based project that manages passcards and visits. It provides functionalities to track active passcards, visits, and storage information. The project uses Django's ORM for database operations and Django's views for handling requests.

## Installation

To install this project, you will need Python and Django installed on your machine. You can then clone this repository and install the necessary dependencies using the following commands:

```bash
git clone https://github.com/Taralas209/DjangoUrok1.git
cd DjangoUrok1
pip install -r requirements.txt
```

## Usage

To run this project, navigate to the project directory and run the following command:

```bash
python main.py
```

This will start the Django development server at 0.0.0.0:8000. 

To access the web application, open your browser and enter the following web address: http://127.0.0.1:8000/

## Models

The project has two main models:

- **Passcard**: Represents a passcard with fields for activity status, creation time, passcode, and owner name.

- **Visit**: Represents a visit with fields for creation time, associated passcard, entry time, and exit time. It also includes methods to calculate the duration of a visit and to check if a visit is long.

## Views

The project includes several views:

- **storage_information_view**: Displays information about ongoing visits.

- **passcard_info_view**: Displays information about a specific passcard's visits.

- **active_passcards_view**: Displays all active passcards.

## License
This project is licensed under the MIT License.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
