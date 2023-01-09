from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="badboy", database="crud")

# Create cursor
my_cursor = mydb.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']

        # Insert into table
        my_cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mydb.commit()
        return 'success'
    return render_template('index.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        id = userDetails['id']

        # Update table
        my_cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
        mydb.commit()
        return 'success'
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        id = userDetails['id']

        # Delete from table
        my_cursor.execute("DELETE FROM users WHERE id=%s", (id,))
        mydb.commit()
        return 'success'
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)

