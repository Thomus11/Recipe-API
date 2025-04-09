import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getRecipes } from '../api/recipes';  // Assuming you have an API function for fetching recipes
import SearchBar from './SearchBar';  // Import the SearchBar component

const RecipeList = () => {
  const [recipes, setRecipes] = useState([]);
  const [filteredRecipes, setFilteredRecipes] = useState([]);

  useEffect(() => {
    // Fetch recipes when the component mounts
    const fetchRecipes = async () => {
      try {
        const data = await getRecipes();
        setRecipes(data);  // Set the fetched recipes
        setFilteredRecipes(data);  // Initially, display all recipes
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    };
    fetchRecipes();
  }, []);  // Empty dependency array ensures this runs once when the component mounts

  const handleSearch = (query) => {
    const lowercasedQuery = query.toLowerCase();
    const filtered = recipes.filter((recipe) =>
      recipe.title.toLowerCase().includes(lowercasedQuery) ||
      recipe.description.toLowerCase().includes(lowercasedQuery)
    );
    setFilteredRecipes(filtered);  // Update the filtered recipes state
  };

  return (
    <div>
      <h1>Recipe List</h1>

      {/* Include the SearchBar component and pass the handleSearch function */}
      <SearchBar onSearch={handleSearch} />

      <ul>
        {filteredRecipes.length > 0 ? (
          filteredRecipes.map((recipe) => (
            <li key={recipe.id}>
              <Link to={`/recipes/${recipe.id}`}>{recipe.title}</Link>
            </li>
          ))
        ) : (
          <p>No recipes found</p>
        )}
      </ul>
    </div>
  );
};

export default RecipeList;
