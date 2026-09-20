from fastapi import FastAPI

app = FastAPI(title='Focal API')

@app.get("/health")
async def health():
    return {'status':'ok'}


@app.get("/health2")
async def health2():
    hey = 2
    h = 3
    return {hey ,'+', h}