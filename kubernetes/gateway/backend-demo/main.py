from fastapi import FastAPI, Request
import uvicorn
import argparse
import config

app = FastAPI()
parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default="config.yml")
args = parser.parse_args()


conf = config.load_config(args.config)


@app.get("/")
def read_root():
    return {"app": conf["app_name"], "version": conf["app_version"]}


@app.post("/")
async def read_root(request: Request):
    body = await request.json()
    headers = request.headers
    return {
        "body": body,
        "headers": headers,
        "app": conf["app_name"],
        "version": conf["app_version"],
    }


if __name__ == "__main__":
    uvicorn.run(app, host=conf["host"], port=conf["port"])
