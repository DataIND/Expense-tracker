# Expense Tracker Application

# Overview
The Expense Tracker is a web application designed to help users efficiently manage their personal finances by tracking income and expenses. Built with Flask, SQLAlchemy, and Chart.js, this application provides a user-friendly interface for logging transactions, categorizing expenses, and visualizing financial data through interactive charts.

# Features
- User-Friendly Interface: Intuitive forms for adding and categorizing expenses.
- Data Visualization: Interactive charts powered by Chart.js to visualize spending patterns and financial trends.
- Database Management: Utilizes SQLite and SQLAlchemy for robust data storage and retrieval, ensuring data integrity and performance.

# Technologies Used
- Flask: Web framework for building the application.
- SQLAlchemy: ORM for database management.
- Flask-WTF: Form handling and validation.
- Chart.js: Library for creating dynamic charts and graphs.

# Getting Started
To run the application locally, follow these steps:

- Clone the repository: git clone <repository-url>
- Install the required dependencies: pip install -r requirements.txt
- Set up the database: flask db init, flask db migrate, flask db upgrade
- Run the application: flask run
- Access the application at http://127.0.0.1:5000
