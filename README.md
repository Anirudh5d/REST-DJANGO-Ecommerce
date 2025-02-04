﻿# REST-DJANGO-Ecommerce Platform
# E-commerce Platform

This project is a Django-based e-commerce platform that provides a comprehensive solution for online shopping. It features user authentication, product management, order tracking, and analytics functionalities. Users can register as customers or vendors, allowing for a seamless shopping and selling experience.

## Features

- **User Authentication**: Users can register and log in to their accounts.
- **Role-based Access**: Different user roles for customers and vendors.
- **Product Management**: Vendors can create, update, delete, and list products.
- **Order Management**: Customers can place orders, and vendors can manage them.
- **Analytics**: Vendors can access sales and inventory reports.
- **Dynamic Home Page**: The home page provides easy navigation for all user roles.
- **Responsive Design**: Beautifully designed web pages using HTML/CSS templates.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ecommerce.git
    cd ecommerce
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your database**: Update `ecommerce/settings.py` with your MySQL database credentials.

5. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Customer User**: Can browse products, place orders, and view order history.
- **Vendor User**: Can manage their own products, view orders, and access analytics.

## API Endpoints

- **Register User**: `/api/register/` (POST)
- **Login User**: `/api/login/` (POST)
- **List Products**: `/api/products/` (GET)
- **Manage Products**: `/api/products/manage/` (GET, POST, PUT, DELETE)
- **Place Order**: `/api/orders/place/` (POST)
- **Track Orders**: `/api/orders/` (GET)

## Technologies Used

- Django
- MySQL
- HTML/CSS
- Bootstrap
- JavaScript

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
