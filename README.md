
# User Registration and Sending Mail Using Gmail

Welcome to the "User Registration and Sending Mail Using Gmail" project! This Django project allows you to register users and send emails using Gmail's SMTP server.

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/user-registration.git
Navigate to the project directory:

cd user-registration


Install dependencies from requirements.txt:

pip install -r requirements.txt

Configuration
Open settings.pyin the user_registration directory.

Replace YOUR_EMAIL with your Gmail address.

Replace YOUR_PASSWORD with your Gmail password or app password if 2-factor authentication is enabled.


Database Migration
Run database migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser
Follow the prompts to enter a username, email address, and password for the superuser.

Running the Server
Run the development server:

python manage.py runserver
Access the application at http://localhost:8000 in your web browser.
