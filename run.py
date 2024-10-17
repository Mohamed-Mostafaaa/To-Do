""" run the flask application"""
from To_Do import create_app, create_database

app = create_app()


if __name__ == "__main__":
    create_database()
    app.run(debug=False,host='0.0.0.0')
