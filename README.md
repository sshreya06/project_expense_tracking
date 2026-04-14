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
<img width="728" height="675" alt="Screenshot 2026-04-14 at 5 44 35 AM" src="https://github.com/user-attachments/assets/4d50ce01-68e4-4239-8702-911bd4d42bb5" />

### Analytics By Category
<img width="727" height="697" alt="Screenshot 2026-04-14 at 5 45 13 AM" src="https://github.com/user-attachments/assets/59b556ea-4c4e-45b8-a858-9917dae199f3" />
<img width="735" height="658" alt="Screenshot 2026-04-14 at 5 45 33 AM" src="https://github.com/user-attachments/assets/6cfe4ee5-6e12-42b4-bf9b-9b3ac049b978" />

### Analytics By Months
<img width="729" height="694" alt="Screenshot 2026-04-14 at 5 45 57 AM" src="https://github.com/user-attachments/assets/549ff598-2a20-4c19-b597-ccb2dd91aa4d" />

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
