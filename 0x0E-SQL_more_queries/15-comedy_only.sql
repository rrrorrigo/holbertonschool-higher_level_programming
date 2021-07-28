-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
SELECT tv_shows.title FROM tv_genres, tv_shows, tv_show_genres
       WHERE tv_genres.name = 'Comedy' AND tv_genres.id = tv_show_genres.genre_id
       AND tv_shows.id = tv_show_genres.show_id
       ORDER BY tv_shows.title;
