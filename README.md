
# Chocolate House Web Application

## Description
Chocolate House is a simple web application designed to manage chocolate-related products, including adding seasonal flavors, ingredients, and customer suggestions, as well as viewing existing data. The application is built using Flask (Python) for the back-end and HTML/CSS for the front-end.

## Features
- **Add Seasonal Flavor**: Allows users to add new chocolate flavors for different seasons.
- **Add Ingredient**: Allows users to add ingredients to the chocolate database.
- **Add Customer Suggestion**: Users can submit their own chocolate-related suggestions.
- **View Data**: Displays existing data for the chocolates, ingredients, and customer suggestions.

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Libraries/Tools**: Flask (for web framework)

## Setup Instructions

### Prerequisites
Ensure that you have the following installed:
- Python (version 3.7 or higher)
- Flask

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/chocolate-house.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd chocolate-house
   ```

3. **Install Required Python Packages**:
   It is recommended to use a virtual environment. You can create one and install the dependencies with:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   You can start the Flask server by running:
   ```bash
   flask run
   ```

5. **Visit the Web Application**:
   Once the server is running, open your browser and visit `http://127.0.0.1:5000/` to see the Chocolate House in action.

## Folder Structure
```
chocolate-house/
├── templates/
│   └── index.html           # Main page of the Chocolate House
├── static/
│   └── css/
│       └── style.css        # Stylesheet for the project
├── app.py                   # Main Flask application
└── requirements.txt         # Python dependencies
```
