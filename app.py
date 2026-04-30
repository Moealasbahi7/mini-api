@app.get("/status")
def status():
    return {"time": str(datetime.now())}

@app.get("/data")
def get_data():
    return {"data": []}

@app.post("/data")
def post_data(item: dict):
    return {"message": "added", "item": item}

@app.get("/poem")
def poem():
    return {"poem": "not ready"}
@app.get("/sana")
def sana():
    return {"message": "added by sana"}