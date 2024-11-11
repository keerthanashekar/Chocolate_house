from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database and create tables
def init_db():
    try:
        conn = sqlite3.connect('chocolate_house1.db')
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
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

# Routes and Functions to add data
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        availability = request.form['availability']
        message = add_seasonal_flavor(name, availability)
        flash(message)
        return redirect(url_for('view_data', table='flavors'))
    return render_template('add_flavor.html')

def add_seasonal_flavor(name, availability):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO seasonal_flavors (name, availability) VALUES (?, ?)', (name, availability))
        conn.commit()
        return "Seasonal flavor added successfully!"
    except sqlite3.Error as e:
        return f"Error adding seasonal flavor: {e}"
    finally:
        conn.close()

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
        return redirect(url_for('view_data', table='ingredients'))
    return render_template('add_ingredient.html')

def add_ingredient(name, quantity):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        return "Ingredient added successfully!"
    except sqlite3.Error as e:
        return f"Error adding ingredient: {e}"
    finally:
        conn.close()

@app.route('/add_suggestion', methods=['GET', 'POST'])
def add_suggestion():
    if request.method == 'POST':
        flavor = request.form['flavor']
        allergy_concern = request.form.get('allergy_concern', '')
        message = add_customer_suggestion(flavor, allergy_concern)
        flash(message)
        return redirect(url_for('view_data', table='suggestions'))
    return render_template('add_suggestion.html')

def add_customer_suggestion(flavor, allergy_concern):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)', 
                       (flavor, allergy_concern))
        conn.commit()
        return "Customer suggestion added successfully!"
    except sqlite3.Error as e:
        return f"Error adding customer suggestion: {e}"
    finally:
        conn.close()

@app.route('/delete_flavor/<int:flavor_id>', methods=['POST'])
def delete_flavor(flavor_id):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM seasonal_flavors WHERE id = ?', (flavor_id,))
        conn.commit()
        flash("Flavor deleted successfully!")
    except sqlite3.Error as e:
        flash(f"Error deleting flavor: {e}")
    finally:
        conn.close()
    return redirect(url_for('view_data', table='flavors'))

@app.route('/delete_ingredient/<int:ingredient_id>', methods=['POST'])
def delete_ingredient(ingredient_id):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM ingredient_inventory WHERE id = ?', (ingredient_id,))
        conn.commit()
        flash("Ingredient deleted successfully!")
    except sqlite3.Error as e:
        flash(f"Error deleting ingredient: {e}")
    finally:
        conn.close()
    return redirect(url_for('view_data', table='ingredients'))

@app.route('/delete_suggestion/<int:suggestion_id>', methods=['POST'])
def delete_suggestion(suggestion_id):
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM customer_suggestions WHERE id = ?', (suggestion_id,))
        conn.commit()
        flash("Suggestion deleted successfully!")
    except sqlite3.Error as e:
        flash(f"Error deleting suggestion: {e}")
    finally:
        conn.close()
    return redirect(url_for('view_data', table='suggestions'))

def view_seasonal_flavors():
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        return cursor.fetchall()
    finally:
        conn.close()

def view_ingredients():
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredient_inventory')
        return cursor.fetchall()
    finally:
        conn.close()

def view_customer_suggestions():
    try:
        conn = sqlite3.connect('chocolate_house1.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer_suggestions')
        return cursor.fetchall()
    finally:
        conn.close()
@app.route('/view_data')
def view_data():
    # Retrieve the 'table' parameter from the query string
    table = request.args.get('table', '')

    # Load data for all tables if no specific table is specified
    data = {
        'flavors': view_seasonal_flavors() if table == 'flavors' or not table else [],
        'ingredients': view_ingredients() if table == 'ingredients' or not table else [],
        'suggestions': view_customer_suggestions() if table == 'suggestions' or not table else [],
    }

    return render_template('view_data.html', **data)



init_db()

if __name__ == "__main__":
    app.run(debug=True)
