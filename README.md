# Bank Security Control Panel

[English](README.md) | [Russian](RU_README.md)

## Description

This is an internal repository for employees of Shining Bank. If you got into this repository by accident, you will not be able to run it, because you do not have access to the database, but you can freely use the code of the layout or see how queries to the database are implemented.

Security desk - a site that can be connected to a remote database with visits and badge cards of employees of our bank

## Installation

To install this project, you will need Python and Django installed on your machine. You can then clone this repository and install the necessary dependencies using the following commands:

```bash
git clone https://github.com/Taralas209/DjangoUrok1.git
cd DjangoUrok1
pip install -r requirements.txt
```
## Environment Setup

Before running the program, you need to set the following environment variables:

- `DB_ENGINE`: Database connection string.
- `DB_HOST`: Database host.
- `DB_PORT`: Port on which your database is running.
- `DB_NAME`: Database name.
- `DB_USER`: Database user name.
- `DB_PASSWORD`: Database user password.
- `SECRET_KEY`: Django secret key. This key is used for cryptographic signatures and should be unique and difficult to guess.
- `DEBUG`: Debug mode. Set the value `'True'` to enable debug mode. Important: Do not use debug mode in production!
- `ALLOWED_HOSTS`: List of hosts allowed to serve your Django application. Hosts should be listed comma-separated. Example: `'localhost,127.0.0.1'`.

## Usage

To run this project, navigate to the project directory and run the following command:

```bash
python manage.py runserver 0.0.0.0:8000
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
