from database.db import get_db_connection

class Expense:
    @staticmethod
    def add_expense(user_id, amount, category, description, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (user_id, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, amount, category, description, date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_expenses_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        expenses = cursor.execute('''
            SELECT * FROM expenses WHERE user_id = ? ORDER BY date DESC
        ''', (user_id,)).fetchall()
        conn.close()
        return expenses
        
    @staticmethod
    def get_expense_by_id(expense_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        expense = cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,)).fetchone()
        conn.close()
        return expense

    @staticmethod
    def update_expense(expense_id, amount, category, description, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses 
            SET amount = ?, category = ?, description = ?, date = ?
            WHERE id = ?
        ''', (amount, category, description, date, expense_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_expense(expense_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_total_expenses(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        result = cursor.execute('SELECT SUM(amount) as total FROM expenses WHERE user_id = ?', (user_id,)).fetchone()
        conn.close()
        return result['total'] if result['total'] else 0.0
