-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name NOT IN (
       SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows
       WHERE tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id
       AND tv_show_genres.genre_id = tv_genres.id)
       ORDER BY tv_genres.name;
