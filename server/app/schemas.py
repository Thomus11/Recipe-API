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
