from flask import Flask,render_template,request,redirect,url_for,flash,session
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    """con=sql.connect("db_villa.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from villa")
    data=cur.fetchall()"""
    return render_template("index.html")

@app.route("/home_villa")
def home_villa():
    
    con=sql.connect("db_villa.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from villa")
    data=cur.fetchall()
    return render_template("home_villa.html",datas=data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
 
        # Insert user into the database
        con = sql.connect('db_villa.db')
        cur = con.cursor()
        flash('Registration Successful','success')
        cur.execute('INSERT INTO register (name,email,password,confirmpassword) VALUES (?, ?, ?, ?)', (name, email, password, confirmpassword))
        con.commit()
        con.close()
 
        return redirect(url_for('index'))
 
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
 
        # Check if the username and password match a user in the database
        con = sql.connect('db_villa.db')
        cur = con.cursor()
        flash('Login Successful','success')
        
        cur.execute('SELECT * FROM register WHERE email = ? AND password = ?', (email, password))
        user = cur.fetchone()
        con.close()
       
 
        if user:
            # If the user exists, set up a session and redirect to the home page
            session['user_id'] = user[0]
            return redirect(url_for('index'))
 
    return render_template('login.html')
 



@app.route("/add_villa",methods=['POST','GET'])
def add_villa():
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        price=request.form['price']
        sqft=request.form['sqft']
        occupancy=request.form['occupancy']
        con=sql.connect("db_villa.db")
        cur=con.cursor()
        cur.execute("insert into villa(UNAME,CONTACT,PRICE,SQFT,OCCUPANCY) values (?,?,?,?,?)",(uname,contact,price,sqft,occupancy))
        con.commit()
        flash('Villa Added','success')
        return redirect(url_for("home_villa"))
    return render_template("add_villa.html")

@app.route("/edit_villa/<string:uid>",methods=['POST','GET'])
def edit_villa(uid):
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        price=request.form['price']
        sqft=request.form['sqft']
        occupancy=request.form['occupancy']
        con=sql.connect("db_villa.db")
        cur=con.cursor()
        cur.execute("update villa set UNAME=?,CONTACT=?,PRICE=?,SQFT=?,OCCUPANCY=? where UID=?",(uname,contact,price,sqft,occupancy,uid))
        con.commit()
        flash('Villa Updated','success')
        return redirect(url_for("home_villa"))
    con=sql.connect("db_villa.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from villa where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit_villa.html",datas=data)
    
@app.route("/delete_villa/<string:uid>",methods=['GET'])
def delete_villa(uid):
    con=sql.connect("db_villa.db")
    cur=con.cursor()
    cur.execute("delete from villa where UID=?",(uid,))
    con.commit()
    flash('Villa Deleted','warning')
    return redirect(url_for("home_villa"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)