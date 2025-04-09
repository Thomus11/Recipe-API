from flask import Blueprint, request, jsonify
from .models import db, Recipe, User, Review
from .schemas import recipe_schema, recipes_schema, review_schema, reviews_schema 

api_bp = Blueprint('api', __name__)


@api_bp.route("/")
def index():
    return jsonify({"message": "Welcome to the Recipe API!"})

# Recipe routes
@api_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    try:
        new_recipe = Recipe(
            title=data['title'],
            ingredients=data['ingredients'],
            instructions=data['instructions'],
            image_url=data.get('image_url'),
            created_by_user_id=data['created_by_user_id']
        )
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.jsonify(new_recipe), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return recipes_schema.jsonify(recipes)


@api_bp.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return recipe_schema.jsonify(recipe)


@api_bp.route('/recipes/<int:id>', methods=['PATCH'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    data = request.get_json()

    recipe.title = data.get('title', recipe.title)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.instructions = data.get('instructions', recipe.instructions)
    recipe.image_url = data.get('image_url', recipe.image_url)

    db.session.commit()
    return recipe_schema.jsonify(recipe)

@api_bp.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": f"Recipe {id} deleted"})


#reviews routes
@api_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    try:
        new_review = Review(
            content = data['content'],
            rating = data['rating'],
            timestamp = data['timestamp']
        )
        db.session.add(new_review)
        db.session.commit()
        return review_schema.jsonify(new_review), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@api_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return reviews_schema.jsonify(reviews)


@api_bp.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get_or_404(id)
    return review_schema.jsonify(review)


@api_bp.route('/reviews/<int:id>', methods=['PATCH'])
def update_review(id):
    review = Review.query.get_or_404(id)
    data = request.get_json()

    review.content = data.get('content', review.content)
    review.rating = data.get('rating', review.rating)

    db.session.commit()
    return review_schema.jsonify(review)

@api_bp.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Review {id} deleted"})