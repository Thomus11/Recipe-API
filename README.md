Recipe Finder Maker
Recipe Finder Maker is a full-stack application designed to allow users to browse, create, review, and manage recipes. It consists of two main parts:

Backend: A Python-based backend using Flask to handle API routes, user authentication, and data management.

Frontend: A React-based frontend that communicates with the backend to provide users with an interactive interface to search, create, and manage recipes.

This project allows users to:

Create new recipes.

View a list of recipes.

Add, update, and delete their own recipes.

Favorite recipes and leave reviews.

Project Structure
bash
Copy
recipe-finder-maker/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── init.py
│   │   │   ├── user.py
│   │   │   ├── recipe.py
│   │   │   ├── review.py
│   │   │   └── favorite.py
│   │   ├── routes/
│   │   │   ├── init.py
│   │   │   ├── auth.py
│   │   │   ├── recipes.py
│   │   │   ├── reviews.py
│   │   │   └── favorites.py
│   │   ├── schemas/
│   │   │   ├── init.py
│   │   │   ├── user_schema.py
│   │   │   ├── recipe_schema.py
│   │   │   ├── review_schema.py
│   │   │   └── favorite_schema.py
│   │   ├── utils/
│   │   │   └── auth.py
│   │   ├── config.py
│   │   ├── extensions.py
│   │   └── main.py
│   ├── migrations/
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── RecipeList.jsx
│   │   │   ├── RecipeDetail.jsx
│   │   │   ├── RecipeForm.jsx
│   │   │   ├── ReviewForm.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── SearchBar.jsx
│   │   ├── pages/
│   │   │   ├── RecipesPage.jsx
│   │   │   ├── RecipeDetailPage.jsx
│   │   │   ├── MyRecipesPage.jsx
│   │   │   ├── CreateRecipePage.jsx
│   │   │   └── FavoritesPage.jsx
│   │   ├── api/
│   │   │   ├── recipes.js
│   │   │   ├── reviews.js
│   │   │   ├── favorites.js
│   │   │   └── auth.js
│   │   ├── utils/
│   │   │   └── validators.js
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── routes.jsx
│   └── package.json
│
├── .env
├── README.md
└── .gitignore
Features
Backend
Flask-based API: The backend is built using Flask, and it provides endpoints to interact with the recipes, reviews, favorites, and user authentication.

Authentication: Handles user sign-up and login with token-based authentication (using JWT).

Database Models: Defines models for users, recipes, reviews, and favorites using SQLAlchemy ORM.

API Routes: Endpoints for creating, reading, updating, and deleting recipes, as well as managing reviews and favorites.

Frontend
React-based Frontend: The frontend is built using React. The app communicates with the backend via API calls to create and manage recipes.

Responsive Pages: Includes pages like a recipe list, recipe details, my recipes, and favorites.

Forms: Users can add new recipes, update them, and leave reviews for existing recipes.

Navigation: The app provides a navigation bar that allows users to easily access different sections, such as creating a recipe or viewing favorites.

Technologies Used
Backend
Flask: A lightweight Python web framework for building the backend API.

SQLAlchemy: ORM for handling database operations in a Pythonic way.

JWT (JSON Web Tokens): For handling user authentication.

SQLite: Used as the database for storing users, recipes, reviews, and favorites data (can be switched to other databases).

Flask-Migrate: For database migrations.

Frontend
React: A JavaScript library for building user interfaces.

Axios: For making API calls to the backend.

React Router: For handling routing in the frontend.

Bootstrap / CSS: For responsive and styled components.

Installation
Backend
Clone the repository:

bash
Copy
git clone https://github.com/your-username/recipe-finder-maker.git
cd recipe-finder-maker/backend
Create a virtual environment:

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up environment variables: Create a .env file in the backend directory and add the necessary environment variables, such as the secret key for JWT and database URL.

Example:

ini
Copy
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///recipes.db
Run migrations:

bash
Copy
flask db upgrade
Run the backend:

bash
Copy
flask run
Frontend
Navigate to the frontend directory:

bash
Copy
cd ../frontend
Install dependencies:

bash
Copy
npm install
Create a .env file for the frontend to store the backend API URL:

ini
Copy
REACT_APP_API_URL=http://localhost:5000
Run the frontend:

bash
Copy
npm start
The React app will open in your browser at http://localhost:3000.

API Endpoints
Authentication
POST /auth/signup: Create a new user.

POST /auth/login: Login and get a JWT token for authentication.

Recipes
GET /recipes: Get all recipes.

POST /recipes: Create a new recipe.

GET /recipes/:id: Get details of a specific recipe.

PUT /recipes/:id: Update a specific recipe.

DELETE /recipes/:id: Delete a specific recipe.

Reviews
POST /reviews: Add a review for a recipe.

GET /reviews/:recipe_id: Get all reviews for a recipe.

Favorites
POST /favorites: Add a recipe to favorites.

GET /favorites: Get all favorite recipes for the user.

DELETE /favorites/:recipe_id: Remove a recipe from favorites.

Running Tests
Backend Tests:

Inside the backend directory, run the following to execute unit tests:

bash
Copy
pytest
Frontend Tests:

Run the following to execute frontend tests using Jest:

bash
Copy
npm test
Contributing
Fork the repository.

Create a new branch for your feature (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to your branch (git push origin feature-name).

Create a new pull request.

License/creators
This project has been created by members of group7, phase 4 of Moringa Schools Software Engineering course

