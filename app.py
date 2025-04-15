from flask import Flask, render_template, request, redirect, url_for
import bcrypt

app = Flask(__name__)

# Simulated user (demo only)
users = {
    'admin': {
        'password_plain': 'admin123',
        'password_hashed': bcrypt.hashpw(b'admin123', bcrypt.gensalt())
    }
}

@app.route('/')
def home():
    return redirect(url_for('login_insecure'))

@app.route('/login-insecure', methods=['GET', 'POST'])
def login_insecure():
    error = ''
    success = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password_plain'] == password:
            success = True
        else:
            error = 'Invalid credentials.'
    return render_template('login_insecure.html', error=error, success=success)

@app.route('/login-secure', methods=['GET', 'POST'])
def login_secure():
    error = ''
    success = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode()
        if username in users and bcrypt.checkpw(password, users[username]['password_hashed']):
            success = True
        else:
            error = 'Invalid credentials.'
    return render_template('login_secure.html', error=error, success=success)

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)

