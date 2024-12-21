CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    quantity FLOAT NOT NULL,
    unit VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS update_ingredients_updated_at
AFTER UPDATE ON ingredients
FOR EACH ROW
BEGIN
    UPDATE ingredients SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    ingredients TEXT NOT NULL,
    preparation_time INT NOT NULL,
    cuisine_type VARCHAR(100),
    taste VARCHAR(100),
    reviews TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS update_recipes_updated_at
AFTER UPDATE ON recipes
FOR EACH ROW
BEGIN
    UPDATE recipes SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;