from flask import Flask, redirect, url_for
from database.db import init_db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.transactions import transactions_bp
import os

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' # For sessions and flashes

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(transactions_bp)

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    # Initialize DB if not exists
    if not os.path.exists('expense_tracker.db'):
        init_db()
    app.run(debug=True)
