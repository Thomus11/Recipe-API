import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from server.app import app
from server.extensions import db

with app.app_context():
    db.create_all()
    print("Database tables created successfully")
