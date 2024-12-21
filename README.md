# Mofa's Kitchen Buddy

Mofa's Kitchen Buddy is a backend system designed to help manage ingredients and suggest recipes based on available items at home. The application leverages a Large Language Model (LLM) to interact with users and provide tailored recipe recommendations.

## Features

- **Ingredient Management**: Add, update, and retrieve available ingredients.
- **Recipe Retrieval**: Parse and store recipe details from saved images or text files.
- **Chatbot Integration**: Interact with a chatbot to receive recipe suggestions based on user preferences and available ingredients.

## Project Structure

```
mofas-kitchen-buddy
├── src
│   ├── app.py                # Main entry point of the application
│   ├── database
│   │   └── schema.sql        # Database schema for ingredients and recipes
│   ├── api
│   │   ├── ingredients.py     # API for managing ingredients
│   │   ├── recipes.py         # API for managing recipes
│   │   └── chatbot.py         # API for chatbot interactions
│   ├── models
│   │   ├── ingredient.py      # Ingredient model
│   │   └── recipe.py          # Recipe model
│   ├── services
│   │   ├── ingredient_service.py # Business logic for ingredient management
│   │   ├── recipe_service.py   # Business logic for recipe management
│   │   └── chatbot_service.py   # Business logic for chatbot interactions
│   └── utils
│       └── ocr.py             # Utility functions for OCR
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── my_fav_recipes.txt         # Combined text of favorite recipes
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mofas-kitchen-buddy.git
   cd mofas-kitchen-buddy
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database by running the SQL schema:
   ```
   # Use your preferred database management tool to execute schema.sql
   ```

4. Run the application:
   ```
   python src/app.py
   ```

## Usage

- Use the API endpoints to manage ingredients and recipes.
- Interact with the chatbot to get personalized recipe suggestions based on your preferences.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.