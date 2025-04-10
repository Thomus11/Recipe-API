from . import ma
from .models import User, Recipe, Review, Favorite

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
        include_fk = True

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True

class FavoriteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Favorite
        load_instance = True
        include_fk = True


recipe_schema = RecipeSchema()        # Instance for a single recipe
recipes_schema = RecipeSchema(many=True) # Instance for multiple recipes (e.g., a list of recipes)
review_schema = ReviewSchema()        # Instance for a single review
reviews_schema = ReviewSchema(many=True) # Instance for multiple reviews (e.g., a list of recipes)