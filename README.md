## Simple calculator
This project allows the calculation of simple arithmetic operations
 
# Local installation and execution

1. Get the code:

        git clone <repo>

2. Execute the docker build:

        docker build -t calculator .

3. Start server:

        docker run -p 8000:8000 -t calculator

4. Run!

        curl --request POST 'http://localhost:8000/calculator/' \
             --header 'Content-Type: application/json' \
             --data-raw '{"operation": "2 + 3"}'

# Calculator api
The calculator contains the following endpoints:

### GET Request

    GET http://localhost:8000/calculator/
    Response application/json
    
### POST Request

    POST http://localhost:8000/calculator/
    Body Example value: {"operation": "2 + 3"}
    Content type application/json
    Response application/json