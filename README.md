
# 🌐 Django Media Server with AWS S3 Integration

A Django project demonstrating how to efficiently manage and serve user-uploaded media files using Amazon S3. Ideal for scaling web applications beyond local storage.

---

## ✨ Features

- 🔐 Secure credentials via `.env` and `python-dotenv`
- ☁️ AWS S3 integration for scalable media storage
- ⚙️ Django 5.2 with modern Python packaging
- 🗃️ Uses SQLite3 for development database
- 🖼️ Upload and serve media without overloading your server

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abhishek173/djangomediaonserver.git
cd djangomediaonserver
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your_secret_key

# AWS S3 Settings
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=your_region
```

> 🔒 **Important:** Never expose real secrets or keys. Use `.env` for local development and configure environment variables securely in production.

### 5️⃣ Apply Migrations & Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 Requirements

All required packages are listed in [`requirements.txt`](./requirements.txt), including:

- `Django`
- `boto3`
- `django-storages`
- `python-dotenv`
- `pillow`
- `sqlparse`
- and more...

---

## 📁 Project Structure

```
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
├── your_django_app/
│   └── ...
```

---

## 🛡️ Security Best Practices

- ✅ Never commit `.env` or sensitive files to version control.
- ✅ Add `.env`, `db.sqlite3`, `__pycache__/`, and other artifacts to `.gitignore`.
- ✅ Use IAM roles and environment variables in production.

---



---

### ❤️ Contributions

Pull requests, stars, and feedback are welcome! Let's make Django projects cleaner and more scalable together 🚀
