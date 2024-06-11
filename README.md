# Addition FastAPI Project

This project demonstrates a FastAPI application organized using the MVC (Model-View-Controller) pattern. It includes an endpoint to perform addition on input lists of integers using Python's multiprocessing library, with appropriate error handling and logging for debugging and monitoring activities.


## Setup

### 1. Clone the repository

```bash
git clone https://github.com/audumbarchavan1988/fastapi_project.git
cd fastapi_project

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python app/main.py

API Endpoint
POST /add/
This endpoint accepts a list of lists of integers and returns the sum of each list.

URL: http://127.0.0.1:8000/add/

Method: POST

Request Format:

  {
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
    }

To Run the tests

python -m unittest discover -s tests
