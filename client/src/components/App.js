import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import RecipesPage from "./pages/RecipesPage";
import RecipeDetailPage from "./pages/RecipeDetailPage";
import MyRecipesPage from "./pages/MyRecipesPage";
import CreateRecipePage from "./pages/CreateRecipePage";
import FavoritesPage from "./pages/FavoritesPage";

function App() {
  const [recipes, setRecipes] = useState([]);
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    // Example fetching recipes from an API or local storage
    fetchRecipes();
  }, []);

  const fetchRecipes = async () => {
    // Fetch recipes from an API or your data source
    const response = await fetch("/api/recipes");
    const data = await response.json();
    setRecipes(data);
  };

  const addFavorite = (recipe) => {
    setFavorites((prevFavorites) => [...prevFavorites, recipe]);
  };

  const removeFavorite = (recipeId) => {
    setFavorites((prevFavorites) =>
      prevFavorites.filter((recipe) => recipe.id !== recipeId)
    );
  };

  return (
    <Router>
      <div className="App">
        <h1>Recipe App</h1>
        <Routes>
          <Route path="/" element={<RecipesPage recipes={recipes} addFavorite={addFavorite} />} />
          <Route path="/recipe/:id" element={<RecipeDetailPage recipes={recipes} />} />
          <Route path="/my-recipes" element={<MyRecipesPage />} />
          <Route path="/create-recipe" element={<CreateRecipePage />} />
          <Route path="/favorites" element={<FavoritesPage favorites={favorites} removeFavorite={removeFavorite} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
