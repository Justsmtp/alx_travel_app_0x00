# alx_travel_app_0x00

## 📍 Project Overview

`alx_travel_app_0x00` is a Django-based web application designed to manage travel listings, bookings, and reviews. This version focuses on database modeling, API serialization, and data seeding.

---

## 🛠 Features

- Custom `Listing`, `Booking`, and `Review` models
- User-based relationships with bookings and reviews
- API-ready serializers for Listings and Bookings
- Management command to seed the database with sample listings

---

## 📂 Project Structure

alx_travel_app_0x00/
├── listings/
│ ├── models.py
│ ├── serializers.py
│ ├── management/
│ │ └── commands/
│ │ └── seed.py
├── alx_travel_app/
│ └── settings.py
├── manage.py
└── README.md



---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
Create and activate a virtual environment


python -m venv venv
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Apply migrations


python manage.py makemigrations
python manage.py migrate
Run the development server


python manage.py runserver
🧪 Seeding the Database
To populate the database with sample listings, run:


python manage.py seed
This will add 10 sample listings with random locations and prices.

🧱 Models Summary
Listing
title

description

location

price_per_night

available

Booking
listing (ForeignKey)

user (ForeignKey)

check_in

check_out

Review
listing (ForeignKey)

user (ForeignKey)

rating

comment

created_at

📦 Serializers
ListingSerializer

BookingSerializer

✅ To Do
Add views and endpoints for Listings and Bookings

Implement authentication and permissions

Add review APIs and validations

Write unit tests for models and APIs

📄 License
This project is licensed for educational use under the MIT License.