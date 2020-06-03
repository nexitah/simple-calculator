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
