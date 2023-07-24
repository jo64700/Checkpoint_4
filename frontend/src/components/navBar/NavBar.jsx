import React from 'react'
import { NavLink } from 'react-router-dom';
import Navigation from '../Navigation';
import './NavBar.css'


const NavBar = () => {
  return (
    <div className='navbar-container'>
        
        <Navigation />
        
    </div>
  )
}

export default NavBar