SELECT tile FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN stars ON ratings.movie_id = stars.movie_id
WHERE stars.person_id =
(
    SELECT id FROM people
    WHERE name = 'Chadwick Boseman'
)
ORDER BY ratings DSC
LIMIT 5
