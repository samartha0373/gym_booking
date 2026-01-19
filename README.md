# Gym Booking System

A simple gym booking system designed to manage user accounts and customer details efficiently. This project uses two database tables: `account_details` and `customer_details`.

## Features

- User Account Management     
    - Booking in/out

- Customer Management
  - Add customer details
  - View customer records
  - Update customer information

## Database Tables

### 1. account_details
- account_id
- username
- password
- email
- sign_in/out
- in/out_time

### 2. customer_details
- customer_id
- full_name
- phone_number
- membership_type
- booking_date

## Technologies Used

- Programming Language: Python
- Database: MySQL
- Interface: Command Line

## Getting Started

1. Clone the repository  
   ```bash
   git clone <https://github.com/samartha0373/gym_booking>
2. run the file in sequence:   
- 'connection_test.py'
- 'create_database.py'
- 'create_tables.py'
- 'insert-data.py'

