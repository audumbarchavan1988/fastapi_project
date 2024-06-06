from model.calculator_model import add_list
from view.calculator_view import display_result
import time

def perform_addition(list):
    result = add_list(list)
    display_result(result)


def process_batch(batch_id, payload):
    started_at = time.time()
    response = [add_list(sublist) for sublist in payload]
    completed_at = time.time()
    display_result(batch_id, response, started_at, completed_at)
