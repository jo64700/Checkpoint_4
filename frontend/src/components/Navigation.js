import React from 'react'
import { NavLink } from 'react-router-dom'

const Navigation = () => {
  return (
    <div className='navigation'>
        <ul className='nav-list'>
            <NavLink className="lien" to="/" >
                <li className="nav-item">Accueil</li>
            </NavLink>
            <NavLink className="lien" to='/fabricant'>
                <li className="nav-item">Fabricant</li>
            </NavLink>
            <NavLink className="lien">
                <li className="nav-item">Modele</li>
            </NavLink>
        </ul>
    </div>
  )
}

export default Navigation