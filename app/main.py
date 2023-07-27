"""Runner for the FastAPI server."""

import logging
import uvicorn


# set up logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="pfred.log",
    filemode="a",
    datefmt="[ %X ]",
)

# create logger
logger = logging.getLogger("pfred")


if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
