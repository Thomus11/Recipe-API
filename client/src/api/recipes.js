const BASE_URL = 'http://localhost:5000/api';

export const createRecipe = async ({ title, ingredients, instructions, image_url }) => {
  const token = localStorage.getItem('token');

  const res = await fetch(`${BASE_URL}/recipes`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      title,
      ingredients,
      instructions,
      image_url,
    }),
  });

  const data = await res.json();
  return data;
};