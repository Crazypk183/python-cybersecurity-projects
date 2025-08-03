from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pw}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            message = "Login successful"
        else:
            message = "Invalid credentials"
    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{message}}</p>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
  
