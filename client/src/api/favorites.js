const BASE_URL = 'http://localhost:5000/api';

export const addFavorite = async (recipeId) => {
  const token = localStorage.getItem('token');

  const res = await fetch(`${BASE_URL}/favorites/add/${recipeId}`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await res.json();
  return data;
};

export const getFavorites = async () => {
  const token = localStorage.getItem('token');

  const res = await fetch(`${BASE_URL}/favorites`, {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await res.json();
  return data;
};
