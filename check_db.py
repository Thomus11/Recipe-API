import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

from server.app import app, db
from server.models import User, Recipe, Review, Favorite

with app.app_context():
    print("Database location:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("\nTables in database:")
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    print(inspector.get_table_names())
    
    print("\nUser columns:")
    print([column.name for column in User.__table__.columns])
    
    print("\nSample data:")
    print("Users:", User.query.count())
    print("Recipes:", Recipe.query.count())
