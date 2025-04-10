const BASE_URL = 'http://localhost:5000/api';

export const register = async (userData) => {
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  const data = await res.json();
  return data;
};

export const login = async (credentials) => {
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(credentials),
  });

  const data = await res.json();

  if (data.token) {
    localStorage.setItem('token', data.token);
  }

  return data;
};

export const logout = () => {
  localStorage.removeItem('token');
};