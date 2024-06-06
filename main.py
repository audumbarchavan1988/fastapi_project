from fastapi import FastAPI, Request
from pydantic import BaseModel
from controller.calculator_controller import process_batch

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

class BatchData(BaseModel):
    batchid: str
    payload: list[list[int]]

@app.post("/add/")
async def main(request: Request):
    """
    Function to process batch data for addition.
    """
    data = await request.json()
    batch_data = BatchData(**data)
    batch_id = batch_data.batchid
    payload = batch_data.payload
    process_batch(batch_id, payload)
    return {"status": "success"}

if __name__ == "__main__":
    main()

