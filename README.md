# crud_ops
simple crud operations using python flask with sql_connector

Flask CRUD Operation

This is a simple application that demonstrates how to perform basic CRUD operations using Flask. The application consists of three pages: index, update, and delete.

Index page: This page allows users to enter their name and email address. When the user submits the form, the data is stored in a MySQL database.

Update page: This page allows users to update their name and email address. When the user submits the form, the data is updated in the MySQL database.

Delete page: This page allows users to delete their data from the MySQL database. When the user submits the form, the data is deleted from the database.

The application uses a MySQL database to store the data. The database connection is established using the mysql.connector library. The cursor object is used to execute SQL queries and commit changes to the database.

The application is written using the Flask framework. The index page is rendered using the render_template() function. The update and delete pages use the request object to fetch form data and execute SQL queries.

about db connection

This application uses a MySQL database to store the data. The database connection is established using the mysql.connector library. The mydb object is used to connect to the database and the my_cursor object is used to execute SQL queries and commit changes to the database.
