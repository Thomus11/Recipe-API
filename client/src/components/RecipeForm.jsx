import React, { useState } from 'react';
import { createRecipe } from '../api/recipes';  // Assuming you have an API function to create recipes

const RecipeForm = () => {
  const [title, setTitle] = useState(''); 
  const [description, setDescription] = useState('');
  const [ingredients, setIngredients] = useState('');
  const [instructions, setInstructions] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const recipeData = {
        title,  
        description,
        ingredients: ingredients.split(','),  
        instructions,
      };
      await createRecipe(recipeData);
      alert('Recipe created successfully!');
    } catch (error) {
      console.error('Error creating recipe:', error);
      alert('Error creating recipe');
    }
  };

  return (
    <div>
      <h1>Create Recipe</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title</label>  
          <input
            type="text"
            value={title}  
            onChange={(e) => setTitle(e.target.value)}  
            required
          />
        </div>
        <div>
          <label>Description</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Ingredients (comma-separated)</label>
          <input
            type="text"
            value={ingredients}
            onChange={(e) => setIngredients(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Instructions</label>
          <textarea
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create Recipe</button>
      </form>
    </div>
  );
};

export default RecipeForm;
