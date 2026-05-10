from database.db import get_db_connection

class Income:
    @staticmethod
    def add_income(user_id, amount, source, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO income (user_id, amount, source, date)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, source, date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_income_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        income = cursor.execute('''
            SELECT * FROM income WHERE user_id = ? ORDER BY date DESC
        ''', (user_id,)).fetchall()
        conn.close()
        return income

    @staticmethod
    def get_income_by_id(income_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        income = cursor.execute('SELECT * FROM income WHERE id = ?', (income_id,)).fetchone()
        conn.close()
        return income

    @staticmethod
    def update_income(income_id, amount, source, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE income 
            SET amount = ?, source = ?, date = ?
            WHERE id = ?
        ''', (amount, source, date, income_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_income(income_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM income WHERE id = ?', (income_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_total_income(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        result = cursor.execute('SELECT SUM(amount) as total FROM income WHERE user_id = ?', (user_id,)).fetchone()
        conn.close()
        return result['total'] if result['total'] else 0.0
