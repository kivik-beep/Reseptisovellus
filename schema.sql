CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    instructions TEXT,
    serves INTEGER,
    active INTEGER,
    passive INTEGER
);

CREATE TABLE incredients (
    recipe_id REFERENCES recipe,
    incredient_id REFERENCES incredient;
    quantity DOUBLE,
    scale TEXT
);

CREATE TABLE incredient (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    type TEXT
);

CREATE TABLE favorites {
    user_id REFERENCES users,
    recipe_id REFERENCES recipe
);


