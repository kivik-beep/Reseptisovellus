CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    user_id INTEGER REFERENCES users,
    instructions TEXT,
    serves INTEGER,
    active INTEGER,
    passive INTEGER
);

CREATE TABLE incredient (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    type TEXT
);


CREATE TABLE incredients (
    recipe_id INTEGER REFERENCES recipe,
    incredient_id INTEGER REFERENCES incredient,
    quantity DECIMAL,
    scale TEXT
);

CREATE TABLE favorites (
    user_id INTEGER REFERENCES users,
    recipe_id INTEGER REFERENCES recipe
);


