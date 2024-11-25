import React from "react";
import { useSearchParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import NewsArticleCard from "./NewsArticleCard";

const NewsArticles = () => {
    const [searchParams] = useSearchParams();
    const keyword = searchParams.get("keyword"); // Extract the 'keyword' query parameter

    const [data, setArticlesData] = useState(null);
    const fetchTopicsData = async () => {
        try {
            console.log(`http://localhost:8000/wikinews/api/newsarticles?keyword=${keyword}`);
            const response = await axios.get(`http://localhost:8000/wikinews/api/newsarticles?keyword=${keyword}`);
            setArticlesData(response.articles);
            console.log(response);
        } catch (err) {
            console.log(err);
        }
    };

    useEffect(() => {
        fetchTopicsData();
    }, []);

    return (
        <div>
            <h1>News Articles</h1>
            {/* <NewsArticleCard article={data.articles[0]} /> */}
        </div>
    );
};

export default NewsArticles;
