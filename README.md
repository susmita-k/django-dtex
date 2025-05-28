# django-dtex

A Django application for monitoring employee and contractor activities with risk categorization.

## Features

- Employee & Contractor models
- Activity tracking with risk levels (low, medium, high)
- Admin interface (1. To Manage Users and 2. To Manage Activities for a Specific User )
- Filtering and search
- Warning indicators for high-risk actions

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/susmita-k/django-dtex.git
cd django-dtex

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
