import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const CreateRecipePage = () => {
  const [title, setTitle] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [instructions, setInstructions] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const recipe = { title, ingredients, instructions };

    try {
      const token = localStorage.getItem("token");

      const response = await fetch("http://localhost:5000/api/recipes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`, // remove if not using auth
        },
        body: JSON.stringify(recipe),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Recipe created:", data);

        // Clear form fields
        setTitle("");
        setIngredients("");
        setInstructions("");

        // Redirect to My Recipes page
        navigate("/my-recipes");
      } else {
        const error = await response.json();
        console.error("Failed to create recipe:", error.message);
        alert("Failed to create recipe.");
      }
    } catch (err) {
      console.error("Error:", err);
      alert("Something went wrong. Please try again.");
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Create a New Recipe</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="p-2 border rounded"
          required
        />
        <textarea
          placeholder="Ingredients"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          className="p-2 border rounded"
          required
        />
        <textarea
          placeholder="Instructions"
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
          className="p-2 border rounded"
          required
        />
        <button type="submit" className="bg-green-600 text-white p-2 rounded">
          Create Recipe
        </button>
      </form>
    </div>
  );
};

export default CreateRecipePage;