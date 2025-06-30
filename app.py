from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from threading import Timer
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ghala.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ghala_secret'

db = SQLAlchemy(app)

# Models
class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    payment_method = db.Column(db.String(20))
    config = db.Column(db.String(100))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'))
    product = db.Column(db.String(50))
    total = db.Column(db.Float)
    status = db.Column(db.String(20))
    merchant = db.relationship('Merchant')

# Routes
@app.route('/')
def home():
    return redirect('/merchant/settings')

@app.route('/merchant/settings', methods=['GET', 'POST'])
def merchant_settings():
    if request.method == 'POST':
        merchant = Merchant(
            name=request.form['name'],
            payment_method=request.form['payment_method'],
            config=request.form.get('config')
        )
        db.session.add(merchant)
        db.session.commit()
        return redirect('/order')
    return render_template('merchant_settings.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    merchants = Merchant.query.all()
    if request.method == 'POST':
        order = Order(
            merchant_id=request.form['merchant'],
            product=request.form['product'],
            total=request.form['total'],
            status='pending'
        )
        db.session.add(order)
        db.session.commit()
        Timer(5, simulate_payment, args=[order.id]).start()
        return redirect('/admin/orders')
    return render_template('order.html', merchants=merchants)

@app.route('/admin/orders')
def admin_orders():
    orders = Order.query.all()
    return render_template('admin_orders.html', orders=orders)


@app.route('/simulate/<int:order_id>')
def simulate(order_id):
    simulate_payment(order_id)
    return redirect('/admin/orders')

def simulate_payment(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = 'paid'
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
