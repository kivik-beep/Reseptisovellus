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
    active DECIMAL(5,2),
    passive DECIMAL(5,2)
);

CREATE TABLE incredient (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    type TEXT
);


CREATE TABLE incredients (
    recipe_id INTEGER REFERENCES recipe ON DELETE CASCADE,
    incredient_id INTEGER REFERENCES incredient,
    quantity DECIMAL(5,2),
    scale TEXT
);

CREATE TABLE favorites (
    user_id INTEGER REFERENCES users,
    recipe_id INTEGER REFERENCES recipe
);

CREATE TABLE tag (
    id SERIAL PRIMARY KEY,
    name TEXT,
    recipe_id INTEGER REFERENCES recipe ON DELETE CASCADE
);
