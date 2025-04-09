import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getRecipeById } from '../api/recipes';  // Assuming you have an API function for fetching a recipe by ID
import ReviewForm from './ReviewForm';  // Import the ReviewForm component

const RecipeDetail = () => {
  const { id } = useParams();  // Get the recipe ID from the URL
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    // Fetch recipe details when the component mounts
    const fetchRecipeDetail = async () => {
      try {
        const data = await getRecipeById(id);
        setRecipe(data);  // Set the fetched recipe
      } catch (error) {
        console.error('Error fetching recipe:', error);
      }
    };
    fetchRecipeDetail();
  }, [id]);  // Run effect again if ID changes

  if (!recipe) {
    return <div>Loading...</div>;  // Show loading message if recipe data is still being fetched
  }

  return (
    <div>
      <h1>{recipe.title}</h1>
      <p>{recipe.description}</p>
      <p>Ingredients: {recipe.ingredients.join(', ')}</p>
      <p>Instructions: {recipe.instructions}</p>

      {/* Include the ReviewForm for submitting reviews */}
      <ReviewForm recipeId={recipe.id} />
    </div>
  );
};

export default RecipeDetail;
