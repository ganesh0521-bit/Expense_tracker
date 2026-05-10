from flask import Blueprint, render_template, session, redirect, url_for
from models.expense import Expense
from models.income import Income

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    user_id = session['user_id']
    
    total_income = Income.get_total_income(user_id)
    total_expenses = Expense.get_total_expenses(user_id)
    balance = total_income - total_expenses
    
    recent_expenses = Expense.get_expenses_by_user(user_id)[:5] # get top 5
    recent_income = Income.get_income_by_user(user_id)[:5]
    
    # Get expenses by category for chart
    all_expenses = Expense.get_expenses_by_user(user_id)
    category_data = {}
    for exp in all_expenses:
        cat = exp['category']
        category_data[cat] = category_data.get(cat, 0) + exp['amount']
        
    return render_template('dashboard.html', 
                           total_income=total_income, 
                           total_expenses=total_expenses, 
                           balance=balance,
                           recent_expenses=recent_expenses,
                           recent_income=recent_income,
                           category_labels=list(category_data.keys()),
                           category_values=list(category_data.values()))
