// src/components/RecipeDetail.jsx

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getRecipeById } from '../api/recipes';  // Assuming you have an API function for fetching a recipe by ID

const RecipeDetail = () => {
  const { id } = useParams();  // Get the recipe ID from the URL parameters
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    // Fetch recipe details by ID when the component mounts
    const fetchRecipeDetail = async () => {
      try {
        const data = await getRecipeById(id);
        setRecipe(data);
      } catch (error) {
        console.error('Error fetching recipe:', error);
      }
    };
    fetchRecipeDetail();
  }, [id]);

  if (!recipe) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{recipe.name}</h1>
      <p>{recipe.description}</p>
      <p>Ingredients: {recipe.ingredients.join(', ')}</p>
      <p>Instructions: {recipe.instructions}</p>
    </div>
  );
};

export default RecipeDetail;
