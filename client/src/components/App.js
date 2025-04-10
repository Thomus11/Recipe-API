import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import RecipeList from './components/RecipeList';
import RecipeDetail from './components/RecipeDetail';
import RecipeForm from './components/RecipeForm';

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route path="/" exact component={RecipeList} />
          <Route path="/recipes" exact component={RecipeList} />
          <Route path="/recipes/:id" component={RecipeDetail} />
          <Route path="/create-recipe" component={RecipeForm} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
