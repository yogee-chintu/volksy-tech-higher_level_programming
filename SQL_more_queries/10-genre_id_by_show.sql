-- creating database from hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genres_id FROM tv_shows INNER JOIN tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genres_id ASC;
