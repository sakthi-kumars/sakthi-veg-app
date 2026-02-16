from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Initial Data
inventory = [
    {'item_en': 'Tomato', 'item_ta': 'தக்காளி', 'stock': 50, 'price': 30},
    {'item_en': 'Onion', 'item_ta': 'வெங்காயம்', 'stock': 100, 'price': 45}
]

@app.route('/')
def index():
    total_items = len(inventory)
    total_stock = sum(float(i['stock']) for i in inventory)
    total_value = sum(float(i['stock']) * float(i['price']) for i in inventory)
    
    return render_template('index.html', 
                           inventory=inventory, 
                           total_items=total_items, 
                           total_stock=total_stock, 
                           total_value=total_value)

@app.route('/add', methods=['POST'])
def add_item():
    item_en = request.form.get('item_en')
    item_ta = request.form.get('item_ta')
    stock = request.form.get('stock')
    price = request.form.get('price')
    
    inventory.append({
        'item_en': item_en, 
        'item_ta': item_ta, 
        'stock': stock, 
        'price': price
    })
    return redirect('/')

if __name__ == '__main__':
    # Cloud Deployment-க்கு இந்த போர்ட் செட்டிங் அவசியம்
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)