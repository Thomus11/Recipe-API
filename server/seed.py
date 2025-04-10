from datetime import datetime
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server.app import app, db
from server.extensions import bcrypt
from server.models import User, Recipe, Review, Favorite

def seed_data():
    # === Create Users ===
    user1 = User(name="John Doe", email="john.doe@example.com")
    user1.password = bcrypt.generate_password_hash("password123").decode('utf-8')
    
    user2 = User(name="Jane Smith", email="jane.smith@example.com")
    user2.password = bcrypt.generate_password_hash("password456").decode('utf-8')
    db.session.add_all([user1, user2])
    db.session.commit()  # Commit users first to get their IDs

    # === Create Recipes ===
    recipes = [
        Recipe(
            title="Berry Cobbler",
            ingredients="2 cups mixed berries, 1 cup oatmeal, 1/2 cup brown sugar",
            instructions="Mix ingredients and bake at 375°F for 30 minutes.",
            image_url="https://reallifedinner.com/berry-cobbler-recipe-make-it-for-one-two-or-twenty/",
            created_by_user_id=1
        ),
        Recipe(
            title="Korean Beef Bowl",
            ingredients="1 lb ground beef, 2 tbsp sesame oil, 1/4 cup soy sauce",
            instructions="Cook ground beef, mix with sauce, and serve over rice.",
            image_url="https://realsimplegood.com/korean-beef-bowl/",
            created_by_user_id=2
        ),
        Recipe(
            title="Crustless Chicken Pot Pie",
            ingredients="2 cups chicken stock, 1 cup mixed vegetables, 1/2 cup flour",
            instructions="Simmer chicken stock and vegetables, thicken with flour.",
            image_url="https://realfoodwholelife.com/recipes/20-minute-stovetop-chicken-pot-pie/",
            created_by_user_id=1
        ),
        Recipe(
            title="King Cake",
            ingredients="1 pack cinnamon rolls, colorful sugar, cream cheese frosting",
            instructions="Arrange cinnamon rolls, top with frosting and sugar.",
            image_url="https://www.reallifeathome.com/easy-king-cake-20-minutes/",
            created_by_user_id=2
        ),
        Recipe(
            title="Peanut Butter Layer Cake",
            ingredients="2 cups flour, 1 cup peanut butter, 1 cup sugar",
            instructions="Mix ingredients, bake at 350°F for 25 minutes.",
            image_url="https://www.lifeloveandsugar.com/loaded-peanut-butter-layer-cake/",
            created_by_user_id=1
        ),
        Recipe(
            title="Honey Garlic Shrimp",
            ingredients="1 lb shrimp, 2 tbsp honey, 1 tbsp garlic",
            instructions="Sauté shrimp with honey and garlic for 10 minutes.",
            image_url="https://www.acouplecooks.com/food-recipes/",
            created_by_user_id=2
        ),
        Recipe(
            title="Pizza Soup",
            ingredients="2 cups tomato sauce, 1 cup bell peppers, 1/2 cup Parmesan",
            instructions="Simmer ingredients together for 20 minutes.",
            image_url="https://www.acouplecooks.com/food-recipes/",
            created_by_user_id=1
        ),
        Recipe(
            title="Crispy Avocado Tacos",
            ingredients="2 avocados, 1 cup breadcrumbs, 1 cup black beans",
            instructions="Bread avocado slices, bake at 400°F for 15 minutes.",
            image_url="https://www.acouplecooks.com/food-recipes/",
            created_by_user_id=2
        ),
        Recipe(
            title="Quick Vegan Curry",
            ingredients="1 can coconut milk, 2 tbsp curry powder, 1 cup vegetables",
            instructions="Simmer coconut milk and vegetables with curry powder.",
            image_url="https://www.acouplecooks.com/food-recipes/",
            created_by_user_id=1
        ),
        Recipe(
            title="One-Pan Lemon Herb Roasted Chicken",
            ingredients="1 whole chicken, 2 lemons, 1 tbsp mixed herbs",
            instructions="Roast chicken with lemons and herbs at 375°F for 1 hour.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=2
        ),
        Recipe(
            title="Creamy Tomato Soup",
            ingredients="2 cans tomatoes, 1 onion, 1 clove garlic",
            instructions="Blend ingredients and simmer for 20 minutes.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=1
        ),
        Recipe(
            title="Cheesy Broccoli and Rice Casserole",
            ingredients="2 cups broccoli, 1 cup rice, 1 cup cheese",
            instructions="Mix ingredients and bake at 350°F for 30 minutes.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=2
        ),
        Recipe(
            title="Garlic Parmesan Pasta",
            ingredients="1 lb pasta, 2 tbsp garlic, 1 cup Parmesan cheese",
            instructions="Cook pasta, toss with garlic and Parmesan.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=1
        ),
        Recipe(
            title="Sheet Pan Nachos",
            ingredients="1 bag tortilla chips, 1 cup cheese, 1 cup toppings",
            instructions="Arrange chips, top with cheese and toppings, bake at 400°F for 10 minutes.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=2
        ),
        Recipe(
            title="Slow Cooker Pulled Pork",
            ingredients="2 lbs pork, 1 cup BBQ sauce, 1 onion",
            instructions="Cook pork with BBQ sauce and onion in slow cooker for 8 hours.",
            image_url="https://happymuncher.com/20-genius-recipes-using-regular-ingredients/",
            created_by_user_id=1
        ),
    ]

    db.session.add_all(recipes)
      
      # === Create Reviews ===
    reviews = [
            Review(content="Amazing recipe, highly recommended!", rating=5, recipe_id=1, user_id=2),
            Review(content="Quick and easy, perfect for a busy evening.", rating=4, recipe_id=2, user_id=1),
            Review(content="A bit too salty, but still good.", rating=3, recipe_id=2, user_id=2),
            Review(content="A dessert that's to die for!", rating=5, recipe_id=1, user_id=1),
        ]
    db.session.add_all(reviews)

        # === Create Favorites ===
    favorites = [
            Favorite(user_id=user1.id, recipe_id=2),
            Favorite(user_id=user2.id, recipe_id=1),
            Favorite(user_id=user1.id, recipe_id=1),  # User 1 likes multiple recipes
        ]   
    db.session.add_all(favorites)
    db.session.commit()
    print("Database seeded successfully with users, recipes, reviews, and favorites!")

    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
        seed_data()
