Ghala Technical Intern Challenge

Features
- Merchants can configure their preferred payment method and config values.
- Customers can place mock orders.
- Admin UI to view orders and manually simulate payment confirmation.
- Async payment simulation updates order to 'paid' after 5 seconds.

How It Works
Each merchant's settings are stored in memory with a unique ID. When an order is placed,
the system stores the status as "pending" and simulates payment by updating it to "paid"
after 5 seconds using threading.

Scaling Plan
- Use PostgreSQL or MongoDB for persistence.
- Add Celery with Redis for async job handling.
- Implement real authentication and user separation.
- Use Docker for deployment and load balancing.

Future Extensions
- Commission rate per merchant.
- Payment API integration.
- Order tracking by customer.

- Project Structure
 instance/           # Configuration & database
templates/          # HTML templates
app.py              # Main Flask application
requirements.txt    # Python dependencies
---
Ensure you have the following installed:
Python 3.7+
pip

Setup Instructions
1. Clone the repository
git clone https://github.com/VARANE/<ghala-core-simulation>.git
cd ghala-core-simulation

2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
4. Run the app
python app.py
5. Access in browser:
