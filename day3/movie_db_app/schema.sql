

CREATE TABLE actors (
    id              serial unique,
    first_name      varchar(50),
    last_name       varchar(50),
    industry        varchar(50),
    gender          varchar(1),
    dob             DATE
);


CREATE TABLE movies (
    id          serial unique,
    name        varchar(100),
    director    varchar(100),
    language    varchar(250),
    production  varchar(250),
    rating      REAL
);

CREATE TABLE movieactors(
    movie_id    int references movies(id),
    actor_id    int references actors(id)
);