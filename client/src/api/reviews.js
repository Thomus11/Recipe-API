const BASE_URL = 'http://localhost:5000/api';

export const postReview = async (recipeId, reviewData) => {
  const token = localStorage.getItem('token');

  const res = await fetch(`${BASE_URL}/reviews/${recipeId}/reviews`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(reviewData),
  });

  const data = await res.json();
  return data;
};