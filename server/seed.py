# seed.py
from app import create_app, db
from app.models import User, Recipe, Review
from faker import Faker
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

# Initialize Flask and DB
app = create_app()
app.app_context().push()

fake = Faker()

def seed_users(num_users=5):
    """Seed users with hashed passwords"""
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            password=generate_password_hash("test123")
        )
        db.session.add(user)
    db.session.commit()
    print(f"✅ Seeded {num_users} users")

def seed_recipes(num_recipes=20):
    """Seed recipes with valid user associations"""
    users = User.query.all()
    for _ in range(num_recipes):
        recipe = Recipe(
            title=fake.sentence(nb_words=3).rstrip(".").title(),
            ingredients="\n".join(
                f"- {fake.word().capitalize()} ({random.randint(1, 500)}g)"
                for _ in range(random.randint(3, 8))
            ),
            instructions="\n".join(
                f"{i+1}. {fake.sentence()}"
                for i in range(random.randint(4, 8))
            ),
            created_by_user_id=random.choice(users).id
        )
        db.session.add(recipe)
    db.session.commit()
    print(f"✅ Seeded {num_recipes} recipes")

def seed_reviews(num_reviews=50):
    """Seed reviews with realistic ratings and timestamps"""
    users = User.query.all()
    recipes = Recipe.query.all()
    
    for _ in range(num_reviews):
        # Get random recipe and user (ensuring user didn't review their own recipe)
        recipe = random.choice(recipes)
        user = random.choice([u for u in users if u.id != recipe.created_by_user_id])
        
        review = Review(
            content=fake.paragraph(nb_sentences=random.randint(2, 5)),
            rating=random.randint(1, 5),
            timestamp=datetime.utcnow() - timedelta(days=random.randint(0, 365)),
            recipe_id=recipe.id,
            user_id=user.id
        )
        db.session.add(review)
    db.session.commit()
    print(f"✅ Seeded {num_reviews} reviews")

if __name__ == "__main__":
    seed_users()    # Step 1: Create users
    seed_recipes()  # Step 2: Create recipes
    seed_reviews()  # Step 3: Create reviews