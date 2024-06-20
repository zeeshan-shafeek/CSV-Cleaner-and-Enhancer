
# CSV Cleaner and Enhancer

## Overview
CSV Cleaner and Enhancer is a simple web application that allows users to upload CSV files, clean the data, add new columns, and download the modified CSV file. The application is built using Flask and Pandas.

## Features
- Upload CSV files.
- Remove rows that are completely empty or duplicated.
- Fill empty cells with a user-provided default value (or "0" if no default value is provided).
- Add new columns with user-specified names and values.
- Download the cleaned and modified CSV file.

## Prerequisites
- Python 3.x
- Flask
- Pandas

## Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/zeeshan-shafeek/CSV-Cleaner-and-Enhancer.git
cd CSV-Cleaner-and-Enhancer
```

### Step 2: Create and Activate a Virtual Environment
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`. Open this URL in your web browser to access the web interface.

## Usage
1. **Upload CSV File**:
    - Select a CSV file to upload.
    - Optionally, specify new column names and values to be added.
    - Optionally, specify a default value to fill empty cells (default is "0").

2. **Process and Download**:
    - Click the "Upload and Process" button.
    - The application will process the file and provide a link to download the cleaned and modified CSV file.

## File Structure
- `app.py`: The main Flask application.
- `templates/index.html`: The HTML template for the web interface.
- `uploads/`: Directory to store uploaded CSV files.
- `processed/`: Directory to store processed CSV files.

## Dependencies
- Flask
- Pandas

