drop table movie;

create table movie(
  movie_id SERIAL PRIMARY KEY,
  title varchar(255) not null,
  release_year int,
  genre varchar(255),
  poster_image_url varchar(255),
  summary text
);
CREATE INDEX ON movie (genre);

insert into movie (title, release_year, genre, poster_image_url, summary)
  values (
    'Arrival',
    2016,
    'sci-fi',
    'https://image.tmdb.org/t/p/original/hLudzvGfpi6JlwUnsNhXwKKg4j.jpg',
    'Taking place after alien crafts land around the world, an expert linguist is recruited by the military to determine whether they come in peace or are a threat.'
  );

insert into movie (title, release_year, genre, poster_image_url, summary)
  values (
    'Guardians of the Galaxy Vol. 2',
    2017,
    'sci-fi',
    'https://image.tmdb.org/t/p/original/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg',
    'The Guardians must fight to keep their newfound family together as they unravel the mysteries of Peter Quill''s true parentage.'
  );

insert into movie (title, release_year, genre, poster_image_url, summary)
  values (
    'Moana',
    2016,
    'family',
    'https://image.tmdb.org/t/p/original/z4x0Bp48ar3Mda8KiPD1vwSY3D8.jpg',
    'In Ancient Polynesia, when a terrible curse incurred by Maui reaches an impetuous Chieftain''s daughter''s island, she answers the Ocean''s call to seek out the demigod to set things right.'
  );

insert into movie (title, release_year, genre, poster_image_url, summary)
  values (
    'Cars 3',
    2017,
    'family',
    'https://image.tmdb.org/t/p/original/fyy1nDC8wm553FCiBDojkJmKLCs.jpg',
    'Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen is suddenly pushed out of the sport he loves. To get back in the game, he will need the help of an eager young race technician with her own plan to win, inspiration from the late Fabulous Hudson Hornet, and a few unexpected turns. Proving that #95 isn''t through yet will test the heart of a champion on Piston Cup Racing''s biggest stage!'
  );
