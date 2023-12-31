# Elevator API

The Elevator API is a Django-based RESTful API that allows you to manage elevators and elevator requests in a building. It provides endpoints for creating and updating elevators, associating elevators with floors, managing elevator availability and operational status, and retrieving elevator information.

## Setup

1. Clone the repository:
   git clone <repository_url>
3. Navigate to the project directory:
   cd elevator
5. Install the required dependencies using pip:
   pip install -r requirements.txt
7. Apply the database migrations:
   python manage.py makemigrations
   python manage.py migrate
9. Run the development server:
    python manage.py runserver


The API will be accessible at `http://localhost:8000/`.

## API Endpoints

- `GET /elevators/`: Retrieve the list of elevators.
- `POST /elevators/create/`: Create a new elevator.
- `PUT /elevators/update/<elevator_id>/`: Update an existing elevator.
- `POST /elevators/associate_with_floor/`: Associate an available elevator with a floor.
- `POST /elevators/mark_available/<elevator_id>/`: Mark an elevator as available.
- `POST /elevators/initialize/`: Initialize the elevator system with a specified number of elevators.
- `GET /elevators/available/`: Retrieve the list of available elevators.
- `GET /elevators/non_operational/`: Retrieve the list of non-operational elevators.
- `GET /elevators/status/<elevator_id>/`: Retrieve the status of a specific elevator.
- `GET /elevators/current_floor/<elevator_id>/`: Retrieve the current floor of a specific elevator.
- `GET /requests/`: Retrieve the list of elevator requests.
- `POST /requests/create/`: Create a new elevator request.

## Models

The Elevator API uses the following Django models:

- `Elevator`: Represents an elevator with attributes such as name, current floor, availability, and operational status.
- `Request`: Represents a request associated with an elevator, specifying the floor and direction.
