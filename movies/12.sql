SELECT  title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id IN
(
    SELECT id FROM people
    WHERE name = 'Johnny Depp' OR name = 'Helena Bonham'
)