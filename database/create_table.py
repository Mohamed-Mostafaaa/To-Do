from To_Do import app, db
# from To_Do.models import User, TaskCollaborator, Task, Note

# Create an application context
with app.app_context():
    # Create all tables
    db.create_all()
    db.session.commit()
