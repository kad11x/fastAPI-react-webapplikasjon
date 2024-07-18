import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <NavLink to="/profile">Profile</NavLink>
      <NavLink to="/history">History</NavLink>
      <NavLink to="/workout">Workout</NavLink>
    </nav>
  );
};

export default Navbar;