""" run the flask application"""

from To_Do import create_app, create_database

app = create_app()


if __name__ == "__main__":
    create_database()
<<<<<<< HEAD:run.py
    app.run(debug=True, host="0.0.0.0")
=======
    app.run(debug=True, host='0.0.0.0')
>>>>>>> f4752c7298bea63e65ecac5c8e7fe6c26f175b2e:app.py
