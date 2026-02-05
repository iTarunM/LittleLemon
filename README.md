# Little Lemon Restaurant
### A Django REST API Project as part of Meta Back-End Developer Capstone Project on Coursera

## Project Overview

Little Lemon is a Mediterranean restaurant web application built with Django and Django REST Framework. This project provides both a web interface for browsing the menu and making reservations, as well as REST API endpoints for programmatic access.


## Project Structure

```
littlelemon/
├── manage.py                           # Django management script
├── db.sqlite3 / MySQL Database         # Database file
├── pyvenv.cfg                          # Virtual environment config
├── littlelemon/                        # Main Django project settings
│   ├── settings.py                     # Project settings and configurations
│   ├── urls.py                         # Root URL configuration (API router)
│   ├── asgi.py                         # ASGI configuration
│   ├── wsgi.py                         # WSGI configuration
│   └── __pycache__/
├── restaurant/                         # Main application
│   ├── models.py                       # Database models (Menu, Booking)
│   ├── views.py                        # View functions and API ViewSets
│   ├── serializers.py                  # DRF Serializers for API
│   ├── urls.py                         # Restaurant app URL routing
│   ├── admin.py                        # Django admin configuration
│   ├── apps.py                         # App configuration
│   ├── migrations/                     # Database migrations
│   ├── tests/                          # Test files
│   └── static/                         # Static files (CSS, Images)
│       └── img/                        # Restaurant images and logo
├── templates/                          # HTML templates
│   ├── base.html                       # Base template with header/footer
│   ├── index.html                      # Home page
│   ├── menu.html                       # Menu listing page
│   ├── menu_item.html                  # Individual menu item details
│   ├── book.html                       # Booking/Reservation page
│   ├── about.html                      # About page
│   └── partials/                       # Template partials
│       ├── _header.html                # Navigation header
│       └── _footer.html                # Footer
└── bin/                                # Virtual environment binaries
```

## Key Models

### Menu Model
- **title**: CharField - Name of the menu item
- **price**: DecimalField - Price of the item (max_digits=10, decimal_places=2)
- **inventory**: IntegerField - Number of items in stock

### Booking Model
- **name**: CharField - Customer name
- **no_of_guests**: IntegerField - Number of guests for the reservation
- **booking_date**: DateField - Date of the reservation

## Features

### 1. **Static HTML Content Pages**
Django serves the following pages through template rendering:

- **Home Page** (`/restaurant/`) - Landing page for the restaurant
- **Menu Page** (`/restaurant/menu/`) - Browse all menu items
- **Menu Item Detail** (`/restaurant/menu/<id>/`) - View detailed information about a specific menu item
- **Booking Page** (`/restaurant/book/`) - Make a reservation
- **About Page** (`/restaurant/about/`) - Restaurant information

### 2. **User Authentication & Registration**
Uses Djoser (Django REST Framework authentication package):

- **User Registration** - Create new user accounts
- **Token Authentication** - Secure API access with tokens

### 3. **REST API Endpoints**

#### Authentication Endpoints
```
POST /auth/users/
  - Register a new user
  - Request body: {"username": "user", "password": "pass123"}

POST /auth/users/set_password/
  - Change user password (requires authentication)

POST /auth/token/login/
  - Login and get authentication token
  - Request body: {"username": "user", "password": "pass123"}
  - Returns: {"auth_token": "your_token_here"}
```

#### Menu API Endpoints
```
GET /restaurant/api/menu/
  - Retrieve all menu items
  - No authentication required
  - Returns: List of menu items with title, price, inventory

GET /restaurant/api/menu/<id>/
  - Retrieve a specific menu item by ID
  - No authentication required
  - Returns: Single menu item details

POST /restaurant/api/menu/
  - Create a new menu item
  - Requires authentication (token)
  - Request body: {"title": "Pizza", "price": "12.99", "inventory": 20}

PUT /restaurant/api/menu/<id>/
  - Update a menu item
  - Requires authentication (token)
  - Request body: {"title": "Pizza", "price": "13.99", "inventory": 25}

DELETE /restaurant/api/menu/<id>/
  - Delete a menu item
  - Requires authentication (token)
```

#### Booking API Endpoints
```
GET /restaurant/booking/tables/
  - Retrieve all bookings
  - Requires authentication (token)
  - Returns: List of all bookings

POST /restaurant/booking/tables/
  - Create a new booking
  - Requires authentication (token)
  - Request body: {
      "name": "John Doe",
      "no_of_guests": 4,
      "booking_date": "2026-02-15"
    }

GET /restaurant/booking/tables/<id>/
  - Retrieve a specific booking by ID
  - Requires authentication (token)

PUT /restaurant/booking/tables/<id>/
  - Update a booking
  - Requires authentication (token)

DELETE /restaurant/booking/tables/<id>/
  - Delete a booking
  - Requires authentication (token)
```

## Installation & Setup

### Prerequisites
- Python 3.13+
- Virtual environment (venv)
- MySQL

### Setup Steps

1. **Activate Virtual Environment**
   ```bash
   source bin/activate  # On macOS/Linux
   # or
   Scripts\activate  # On Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Load Sample Menu Data (Fixture)**
   ```bash
   python manage.py loaddata restaurant/fixtures/menu.json
   ```

5. **Create Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

   The server will run at `http://127.0.0.1:8000/`

## Testing Guide

### 1. Testing Static HTML Pages

Open these URLs in your browser:
- **Home**: `http://127.0.0.1:8000/restaurant/`
- **Menu**: `http://127.0.0.1:8000/restaurant/menu/`
- **Menu Item**: `http://127.0.0.1:8000/restaurant/menu/1/`
- **Book Table**: `http://127.0.0.1:8000/restaurant/book/`
- **About**: `http://127.0.0.1:8000/restaurant/about/`

### 2. Testing API Endpoints (Method 1: Django REST Framework Browsable API)

Django REST Framework provides a web interface for testing API endpoints.

1. Navigate to: `http://127.0.0.1:8000/restaurant/api/menu/`
2. You can perform GET, POST, PUT, DELETE operations directly in the browser

### 3. Testing API Endpoints (Method 2: cURL Commands)

#### User Registration
```bash
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

#### User Login (Get Authentication Token)
```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

Save the returned token for authenticated requests:
```
{"auth_token":"your_token_string_here"}
```

#### GET All Menu Items (No Authentication Required)
```bash
curl -X GET http://127.0.0.1:8000/restaurant/api/menu/ \
  -H "Content-Type: application/json"
```

#### GET Specific Menu Item
```bash
curl -X GET http://127.0.0.1:8000/restaurant/api/menu/1/ \
  -H "Content-Type: application/json"
```

#### POST - Create New Menu Item (Requires Authentication)
```bash
curl -X POST http://127.0.0.1:8000/restaurant/api/menu/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{"title":"Pasta Carbonara","price":"14.99","inventory":15}'
```

#### PUT - Update Menu Item (Requires Authentication)
```bash
curl -X PUT http://127.0.0.1:8000/restaurant/api/menu/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{"title":"Updated Dish","price":"15.99","inventory":20}'
```

#### DELETE - Delete Menu Item (Requires Authentication)
```bash
curl -X DELETE http://127.0.0.1:8000/restaurant/api/menu/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

#### GET All Bookings (Requires Authentication)
```bash
curl -X GET http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

#### POST - Create New Booking (Requires Authentication)
```bash
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{"name":"John Doe","no_of_guests":4,"booking_date":"2026-02-15"}'
```

### 4. Testing API Endpoints (Method 3: Postman)

1. **Download Postman** from https://www.postman.com/downloads/
2. **Create a new collection** for Little Lemon API
3. **Add requests** using the endpoint URLs above
4. **Set Authorization** headers with your token from login response
5. **Test all CRUD operations** (Create, Read, Update, Delete)

### 5. Testing Authentication Flow

1. **Register a new user**:
   ```bash
   curl -X POST http://127.0.0.1:8000/auth/users/ \
     -H "Content-Type: application/json" \
     -d '{"username":"newuser","password":"securepass123"}'
   ```

2. **Login to get token**:
   ```bash
   curl -X POST http://127.0.0.1:8000/auth/token/login/ \
     -H "Content-Type: application/json" \
     -d '{"username":"newuser","password":"securepass123"}'
   ```

3. **Use token in subsequent requests**:
   ```bash
   curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token <your_token>" \
     -d '{"name":"John","no_of_guests":2,"booking_date":"2026-02-20"}'
   ```

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/`

- Login with your superuser credentials
- Manage Menu items
- Manage Bookings
- Manage Users

## Technologies Used

- **Django 6.0.1** - Web framework
- **Django REST Framework 3.16.1** - API framework
- **Djoser 2.3.3** - Authentication (user registration and token auth)
- **MySQL** - Database (configurable to SQLite)
- **Python 3.13** - Programming language

## Notes

- Static files (CSS, images) are served from `/restaurant/static/`
- HTML templates are served with Django template engine
- Sample menu items are provided in `restaurant/fixtures/menu.json` and loaded via the setup steps
- Database will be empty until migrations are run and fixtures are loaded
- All API endpoints return JSON responses
- Token authentication is required for bookings and menu management
- Menu browsing does not require authentication
