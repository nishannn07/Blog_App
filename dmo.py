# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# print(dir(db))


# from app import db
# db.session.execute("DROP TABLE IF EXISTS _alembic_tmp_post")
# db.session.commit()


from app import app, db  # replace with your actual app module

from sqlalchemy import text

with app.app_context():
    db.session.execute(text("DROP TABLE IF EXISTS _alembic_tmp_post"))
    db.session.commit()
    print("Temporary table dropped successfully.")
