import React, { useState, useEffect } from 'react';

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState(query);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(query);
    }, 500);  // Wait for 500ms after the user stops typing

    return () => clearTimeout(timer);  // Clean up the timer on every re-render
  }, [query]);

  useEffect(() => {
    onSearch(debouncedQuery);  // Trigger search only when debounced query changes
  }, [debouncedQuery, onSearch]);

  const handleSearch = (e) => {
    e.preventDefault();
    setQuery(e.target.value);  // Update query state on input change
  };

  return (
    <form onSubmit={handleSearch}>
      <input
        type="text"
        value={query}
        onChange={handleSearch}
        placeholder="Search for recipes"
      />
      <button type="submit">Search</button>
    </form>
  );
};

export default SearchBar;
