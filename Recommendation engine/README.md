
# Netflix Movie Recommendation System

## Project Overview

The objective of this project is to develop a recommendation system for Netflix users based on historical ratings data. By utilizing both collaborative filtering techniques (SVD) and content-based filtering (Pearson Correlation), the system predicts movie ratings and recommends movies that are most likely to match users' preferences. The system aims to provide personalized suggestions, improving user experience and engagement on the platform.

## Objective

The main goal of this project is to develop an effective recommendation system capable of:
- Predicting ratings for movies that users haven't rated yet.
- Recommending personalized movie suggestions based on a user's historical preferences.
- Enhancing user engagement by offering highly relevant content recommendations.

## Problem Description

Netflix, like many content platforms, faces the challenge of delivering personalized content recommendations to its vast user base. With millions of movies and shows available, users often struggle to discover new content that aligns with their tastes. The dataset used in this project contains historical movie ratings from users, and the goal is to predict which movies a user might like based on their past interactions and the ratings of other users with similar tastes. A robust recommendation system will help Netflix increase user satisfaction and retention by offering relevant suggestions.

## Scope of the Solution

This solution implements two key recommendation techniques:

1. **Collaborative Filtering using Singular Value Decomposition (SVD):**
   - Leverages historical ratings data to predict ratings for unrated movies and suggest items based on user preferences and the preferences of similar users.

2. **Content-Based Filtering using Pearson Correlation:**
   - Recommends similar movies based on the correlation of user ratings, allowing the system to suggest movies that are similar to the ones the user has rated highly.

The solution includes preprocessing steps such as data cleaning, removing low-rated movies, and handling missing values. The final model predicts ratings for a given user and recommends a list of top 10 movies based on similarity.

## Expected Outcome

The expected outcome is a fully functional recommendation system that:
- Predicts ratings for unrated movies.
- Recommends movies that match a user's preferences.
- Improves user engagement by offering highly relevant movie suggestions.
- Evaluates the model’s performance using cross-validation, RMSE (Root Mean Squared Error), and MAE (Mean Absolute Error).

## Features

The Netflix Movie Recommendation System provides the following features:
- Predicts ratings for movies a user has not yet rated.
- Recommends top 10 movies based on similar user preferences.
- Personalized movie recommendations using both collaborative filtering and content-based methods.
