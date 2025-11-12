from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

def read_sqlite(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
        return None
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)
    products_data = []
    error_message = None

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'products.json')
    csv_path = os.path.join(base_dir, 'products.csv')
    db_path = os.path.join(base_dir, 'products.db')

    if source == 'json':
        products_data = read_json(json_path)
    elif source == 'csv':
        products_data = read_csv(csv_path)
    elif source == 'sql':
        products_data = read_sqlite(db_path)
        if products_data is None:
            error_message = "Database error"
    else:
        error_message = "Wrong source"

    if error_message is None and id_param is not None and products_data is not None:
        try:
            id_int = int(id_param)
            filtered = [p for p in products_data if p['id'] == id_int]
            if not filtered:
                error_message = "Product not found"
            else:
                products_data = filtered
        except ValueError:
            error_message = "Invalid id parameter"

    return render_template('product_display.html',
                           products=products_data,
                           error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
