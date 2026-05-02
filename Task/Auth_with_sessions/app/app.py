from flask import Flask,request,jsonify,render_template,redirect,url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS app(
                   id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   password TEXT
                   )
    ''')
    conn.commit()
    conn.close()
def get_db():
    return sqlite3.connect('app.db')

@app.route('/signup',methods=['GET','POST'])
def signup():
    # data = request.get_json()
    # username = data['username']
    # email = data['email']
    # password = data['password']
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO app(username,email,password) VALUES(?,?,?)",(username,email,hashed_password))
        conn.commit()
        conn.close()

        return redirect(url_for('success'))
    # return jsonify({"massege":"user Createdddd/......."})
    return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM app WHERE email=?",(email,))
        user = cursor.fetchone()
        conn.close()
        print(user)
        if user:
            if check_password_hash(user[3],password):
                session['user_id'] = user[2]
                return redirect(url_for('loged'))
            else:
                return {"massege":"Worng Password"}
    return render_template('login.html')

@app.route('/success')
def success():
    return "Successfully signup ho gaya hai bhai"

@app.route('/loged')
def loged():
    if 'user_id' not in session:
        return redirect(url_for('login'))    
    # return f"You are logged in! Welcome! {session['user_id']}"
    return render_template('logout.html', user_id=session['user_id'])

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)