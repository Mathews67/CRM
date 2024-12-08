// src/components/CrimeCategoryList.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CrimeCategoryList = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        // Fetch crime categories from the API
        axios.get('http://localhost:8000/api/crime-categories/')
            .then((response) => {
                setCategories(response.data);
            })
            .catch((error) => {
                console.error('There was an error fetching the crime categories!', error);
            });
    }, []);

    return (
        <div>
            <h1>Crime Categories</h1>
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>
                        {category.category_name} - {category.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CrimeCategoryList;
