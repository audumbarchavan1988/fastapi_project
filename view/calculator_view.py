def display_result(batch_id, response, started_at, completed_at):
    data = {
        batch_id: response,
        "Started at" : started_at,
        "Completed at" : completed_at
    }
    print(data)    

    return {
        batch_id: response,
        "Started at" : started_at,
        "Completed at" : completed_at
    }
