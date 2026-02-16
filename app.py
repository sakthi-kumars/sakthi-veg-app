from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Inventory Data
inventory = [
    {'item_en': 'Tomato', 'item_ta': 'தக்காளி', 'stock': 50, 'price': 30},
    {'item_en': 'Onion', 'item_ta': 'வெங்காயம்', 'stock': 100, 'price': 45}
]

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    item_en = request.form.get('item_en')
    item_ta = request.form.get('item_ta')
    stock = request.form.get('stock')
    price = request.form.get('price')
    inventory.append({'item_en': item_en, 'item_ta': item_ta, 'stock': stock, 'price': price})
    return redirect('/')

# முக்கியமான மாற்றம்: Render-ன் PORT-ஐக் கண்டறியும் முறை
if __name__ == '__main__':
    # Render தளம் கொடுக்கும் போர்ட்-ஐ இங்கே வாங்குகிறோம்
    port = int(os.environ.get("PORT", 10000))
    # 0.0.0.0 என்பது உலகளாவிய இணைப்பிற்கு அவசியம்
    app.run(host='0.0.0.0', port=port)
