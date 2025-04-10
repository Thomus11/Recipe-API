import React from 'react';
import { useParams } from 'react-router-dom';

const RecipeDetailPage = () => {
  const { id } = useParams();

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Recipe Details</h1>
      <p>Recipe ID: {id}</p>
    </div>
  );
};

export default RecipeDetailPage;