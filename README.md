# Django Media on Server (with AWS S3 Integration)

This is a Django-based web application demonstrating how to manage and serve media files using Amazon S3 cloud storage. It provides a scalable solution for storing user-uploaded media without overloading the local server.

## 🚀 Features

- 🔐 Secure Django project with `.env` configuration
- 🗃️ AWS S3 integration using `django-storages` and `boto3`
- 🖼️ Media handling (upload, retrieve) using cloud storage
- 🔧 Environment variables support via `python-dotenv`
- 🐘 SQLite3 as the default development database

## 📦 Tech Stack

- Python 3
- Django 5.2
- AWS S3
- boto3 & django-storages
- SQLite3
- dotenv for environment management

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add a .env file
Create a .env file in the root directory with your secrets. Example:

env
Copy
Edit
# Django Settings
SECRET_KEY=your_secret_key

# AWS S3 Settings
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=your_region
5. Apply migrations and run the server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Now the application will be accessible at http://127.0.0.1:8000/.

🧾 Requirements
See requirements.txt for all the packages used in the project.

🗃 .gitignore
Sensitive files such as .env, db.sqlite3, and compiled files are excluded from version control via .gitignore.

📁 Directory Structure
bash
Copy
Edit
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
├── your_django_app/
│   └── ...
⚠️ Security Notice
Make sure never to commit your real .env file or credentials to version control. Use environment variables in production for safety.

📜 License
This project is open-source and available under the MIT License.
