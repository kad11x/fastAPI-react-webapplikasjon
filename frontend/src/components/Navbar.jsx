import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Navbar.css';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function Navbar() {
    const navigate = useNavigate();

    const handleLogout = () => {
        // Redirect to the login page
        navigate('/');
    };

    return (
        <div className="navbar-container">
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <a className="navbar-brand" href="/home">Gain</a>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                                <ul className="navbar-nav">
                                    <li className="nav-item dropdown">
                                    <button className="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                                        Services
                                    </button>
                                    <ul className="dropdown-menu dropdown-menu-dark">
                                        <li><a className="dropdown-item" href="/create-templates">Create Templates</a></li>
                                        <li><a className="dropdown-item" href="/workouts">Brows Workout</a></li>
                                    </ul>
                                    </li>
                                </ul>
                                </div>

                            <li className="nav-item">
                            <a className="nav-link active" aria-current="page" href="/profile">Profile</a>
                            </li>
                            <li className="nav-item">
                            <a className="nav-link active" aria-current="page" href="/Ai_page">Ai page</a>
                            </li>
                        </ul>
                        <form className="d-flex">
                            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                            <button className="btn btn-outline-primary" type="submit">Search</button>
                        </form>
                        <button className="btn btn-primary ms-3" onClick={handleLogout}>Log Out</button>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Navbar;
