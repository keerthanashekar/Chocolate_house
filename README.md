# Chocolate_house

# Chocolate House Inventory and Flavor Management

This is a web-based application built with Flask and SQLite to manage a chocolate shop's inventory, seasonal flavors, and customer flavor suggestions. The application provides functionalities to view, add, update, and delete seasonal flavors, ingredient inventory items, and customer suggestions.

## Features

- **View Data**: See lists of all seasonal flavors, ingredients, and customer suggestions.
- **Add Data**: Add new seasonal flavors, ingredients, and customer suggestions.
- **Update Data**: Update existing seasonal flavors and ingredients.
- **Delete Data**: Delete entries for seasonal flavors and ingredients.
- **User-Friendly Interface**: Includes a CSS-styled UI for an enhanced user experience.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLite**: A self-contained, high-reliability, embedded, SQL database engine.
- **HTML/CSS**: For the front-end layout and styling.
- **Jinja2**: Template engine for Python used with Flask.

## Project Structure

- `templates/`: Contains HTML templates for the web pages.
- `static/style.css`: Contains the CSS file for styling.
- `app.py`: Main Flask application file.
- `README.md`: Project documentation.

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/chocolate-house.git
    cd chocolate-house
    ```

2. **Set Up the Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**:
    ```bash
    pip install Flask
    ```

4. **Initialize the Database**:
    The `init_db` function in `app.py` will create the database and tables automatically when the app runs for the first time. Run the following command to start the app and initialize the database:
    ```bash
    python app.py
    ```

5. **Run the Application**:
    ```bash
    flask run
    ```

6. **Access the Application**:
    Open a web browser and go to `http://127.0.0.1:5000` to access the Chocolate House application.

## Usage

1. **Home Page**:
   - Navigate to the home page to see options to view or add data.

2. **View Data**:
   - Go to `/view_data` to see all seasonal flavors, ingredients, and customer suggestions.

3. **Add New Entries**:
   - Use `/add_flavor`, `/add_ingredient`, or `/add_suggestion` to add new flavors, ingredients, or suggestions respectively.

4. **Update and Delete Entries**:
   - Go to the `view_data` page and use the "Update" or "Delete" buttons next to each item to modify or remove entries.



