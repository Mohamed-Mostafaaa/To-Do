from To_Do import app, db

# Create an application context
with app.app_context():
    # Create all tables
    db.create_all()
    db.session.commit()
