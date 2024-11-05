import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Initialize the database and create tables
def init_db():
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        
        # Create tables if they don't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            availability TEXT NOT NULL CHECK(availability IN ('Available', 'Unavailable'))
        )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_suggestion TEXT NOT NULL,
            allergy_concern TEXT
        )''')
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

# Routes and Functions to add data
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_data')
def view_data():
    flavors = view_seasonal_flavors()
    ingredients = view_ingredients()
    suggestions = view_customer_suggestions()
    return render_template('view_data.html', flavors=flavors, ingredients=ingredients, suggestions=suggestions)

@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        availability = request.form['availability']
        message = add_seasonal_flavor(name, availability)
        flash(message)
        return redirect(url_for('view_data'))
    return render_template('add_flavor.html')

@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient_route():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        if quantity.isdigit():
            message = add_ingredient(name, int(quantity))
        else:
            message = "Invalid quantity. Please enter a valid integer."
        flash(message)
        return redirect(url_for('view_data'))
    return render_template('add_ingredient.html')

@app.route('/add_suggestion', methods=['GET', 'POST'])
def add_suggestion():
    if request.method == 'POST':
        flavor = request.form['flavor']
        allergy_concern = request.form.get('allergy_concern', '')
        message = add_customer_suggestion(flavor, allergy_concern)
        flash(message)
        return redirect(url_for('view_data'))
    return render_template('add_suggestion.html')

# Functions to interact with the database
def add_seasonal_flavor(name, availability):
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO seasonal_flavors (name, availability) VALUES (?, ?)', (name, availability))
        conn.commit()
        return "Seasonal flavor added successfully!"
    except sqlite3.Error as e:
        return f"Error adding seasonal flavor: {e}"
    finally:
        conn.close()

def add_ingredient(name, quantity):
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        return "Ingredient added successfully!"
    except sqlite3.Error as e:
        return f"Error adding ingredient: {e}"
    finally:
        conn.close()

def add_customer_suggestion(flavor, allergy_concern):
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)', 
                       (flavor, allergy_concern))
        conn.commit()
        return "Customer suggestion added successfully!"
    except sqlite3.Error as e:
        return f"Error adding customer suggestion: {e}"
    finally:
        conn.close()

def view_seasonal_flavors():
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        flavors = cursor.fetchall()
        return flavors
    except sqlite3.Error as e:
        print(f"Error viewing seasonal flavors: {e}")
        return []
    finally:
        conn.close()

def view_ingredients():
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredient_inventory')
        ingredients = cursor.fetchall()
        return ingredients
    except sqlite3.Error as e:
        print(f"Error viewing ingredients: {e}")
        return []
    finally:
        conn.close()

def view_customer_suggestions():
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer_suggestions')
        suggestions = cursor.fetchall()
        return suggestions
    except sqlite3.Error as e:
        print(f"Error viewing customer suggestions: {e}")
        return []
    finally:
        conn.close()

# Initialize the database
init_db()

if __name__ == "__main__":
    app.run(debug=True)
