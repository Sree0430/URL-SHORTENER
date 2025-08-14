# Django URL Shortener

A simple Django-based URL shortener web application that allows users to generate short links from long URLs and track recent links.

---

## Features

* Accepts long URLs and generates short links
* Optional custom short code for URLs
* Redirects short links to the original URL
* Stores recent URLs and click counts
* Clean and responsive web interface using Bootstrap

---

## Technologies Used

* Python 3.x
* Django 5.x
* Bootstrap 5 (via CDN)
* SQLite (default database)

---

## Folder Structure

```
URL-Shortener/
├── manage.py
├── myproject/
├── urlsapp/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       └── urlsapp/
│           ├── base.html
│           └── index.html
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/URL-Shortener.git
```

2. Navigate into the project folder:

```bash
cd ioss
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Apply migrations:

```bash
python manage.py migrate
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open in browser:

```
http://127.0.0.1:8000/
```

---

## Usage

1. Enter a long URL in the input field.
2. Optionally, provide a custom short code.
3. Click **Generate** to get a short URL.
4. Recent short URLs and click counts are displayed on the page.
5. Click a short URL to test the redirection to the original link.

---

## Optional Features (Extra Points)

* Docker setup for one-command app
