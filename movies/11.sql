SELECT tile FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN stars ON ratings.