from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.expense import Expense
from models.income import Income

transactions_bp = Blueprint('transactions', __name__)

# --- EXPENSE ROUTES ---
@transactions_bp.route('/expenses', methods=['GET', 'POST'])
def manage_expenses():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    user_id = session['user_id']
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        
        Expense.add_expense(user_id, amount, category, description, date)
        flash('Expense added successfully!', 'success')
        return redirect(url_for('transactions.manage_expenses'))
        
    expenses = Expense.get_expenses_by_user(user_id)
    categories = ['Food', 'Travel', 'Shopping', 'Bills', 'Entertainment', 'Health', 'Education', 'Other']
    return render_template('transactions.html', title='Expenses', items=expenses, type='expense', categories=categories)

@transactions_bp.route('/expenses/delete/<int:id>')
def delete_expense(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Expense.delete_expense(id)
    flash('Expense deleted successfully.', 'info')
    return redirect(url_for('transactions.manage_expenses'))

# --- INCOME ROUTES ---
@transactions_bp.route('/income', methods=['GET', 'POST'])
def manage_income():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    user_id = session['user_id']
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        source = request.form['source']
        date = request.form['date']
        
        Income.add_income(user_id, amount, source, date)
        flash('Income added successfully!', 'success')
        return redirect(url_for('transactions.manage_income'))
        
    income = Income.get_income_by_user(user_id)
    return render_template('transactions.html', title='Income', items=income, type='income')

@transactions_bp.route('/income/delete/<int:id>')
def delete_income(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Income.delete_income(id)
    flash('Income deleted successfully.', 'info')
    return redirect(url_for('transactions.manage_income'))
