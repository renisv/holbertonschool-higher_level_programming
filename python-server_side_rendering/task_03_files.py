from flask import Flask, render_template, request
import json
import csv
import os

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
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)
    products_data = []
    error_message = None

    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')

    if source == 'json':
        products_data = read_json(json_path)
    elif source == 'csv':
        products_data = read_csv(csv_path)
    else:
        error_message = "Wrong source"

    if error_message is None and id_param is not None:
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
