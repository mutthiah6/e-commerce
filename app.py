from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'mysecret'


products = [
    {'id': 1, 'name': 'T-Shirt', 'price': 1000},
    {'id': 2, 'name': 'Jeans', 'price': 2500},
    {'id': 3, 'name': 'Jacket', 'price': 4000},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = [p for p in products if p['id'] in session.get('cart', [])]
    total = sum(p['price'] for p in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
