

CREATE TABLE USERPROFILE(
    id      SERIAL,
    name    VARCHAR(250) NOT NULL,
    email   VARCHAR(250) UNIQUE NOT NULL,
    password VARCHAR(72) NOT NULL
);