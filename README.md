<img width="565" alt="Screenshot 2025-05-27 at 10 49 51 PM" src="https://github.com/user-attachments/assets/4c7b85b2-36cc-458d-9d5c-5b4c384ae80a" />
<img width="1435" alt="Screenshot 2025-05-27 at 10 49 30 PM" src="https://github.com/user-attachments/assets/706821ca-4985-415a-93b8-848892e25f00" />
<img width="413" alt="Screenshot 2025-05-27 at 10 49 40 PM" src="https://github.com/user-attachments/assets/8b210519-3aeb-40f6-9e21-602820a698bc" />
<img width="1420" alt="Screenshot 2025-05-27 at 10 49 19 PM" src="https://github.com/user-attachments/assets/1c62d2ee-cbe0-4bcf-9d65-87e2b976d3cf" />
# django-dtex

A Django application for monitoring employee and contractor activities with risk categorization.

## Features

- Worker and WorkerActivity models (dtex/workers/models.py)
- workers/views.py (CRUD operations for Workers and Activities of Selected User)
- Admin interface Templates (1. To Manage Users and 2. To Manage Activities for a Specific User )
- User List with Filtering and search by -
•  Employee/Contractor name
•  Date range
•  Type of activity
•  Risk level
- Warning indicators for high-risk actions - (this one has a small bug)

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
cd dtex
python manage.py migrate

# Start server
python manage.py runserver
