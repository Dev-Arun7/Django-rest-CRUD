# Drinks API

This is a simple Django REST Framework API for managing a collection of drinks.

## Features

- List all drinks
- Create a new drink
- Retrieve details of a specific drink
- Update a specific drink
- Delete a specific drink

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /drinks/ | List all drinks |
| POST   | /drinks/ | Create a new drink |
| GET    | /drinks/<id>/ | Retrieve a specific drink |
| PUT    | /drinks/<id>/ | Update a specific drink |
| DELETE | /drinks/<id>/ | Delete a specific drink |

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drinks-api.git
   cd drinks-api