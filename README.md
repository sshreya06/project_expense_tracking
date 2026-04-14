# Expense Tracking System

A full-stack expense tracking application built with FastAPI, Streamlit, and MySQL.

## Features
- Add and update daily expenses by category
- Analytics breakdown by category with percentage split
- Analytics breakdown by month
- REST API backend with FastAPI
- Interactive frontend with Streamlit

## Screenshots

### Add/Update Expenses
![Add Update](assets/add_update.png)

### Analytics By Category
![Analytics Category](assets/analytics_category.png)

### Analytics By Months
![Analytics Months](assets/analytics_months.png)

## Tech Stack
- **Backend:** Python, FastAPI, MySQL
- **Frontend:** Streamlit
- **Database:** MySQL
- **Testing:** Pytest

## How to Run

### 1. Clone the repository
git clone https://github.com/sshreya06/project_expense_tracking.git
cd project_expense_tracking

### 2. Install dependencies
pip install fastapi uvicorn streamlit mysql-connector-python requests pandas

### 3. Start the FastAPI server
python3 -m uvicorn backend.server:app --reload

### 4. Start the Streamlit frontend
cd frontend
python3 -m streamlit run app.py