import logging
import uvicorn
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()


def main():
    logger.info('Logger configured')
    logger.info('Starting FastAPI application')
    uvicorn.run(app, port=8080, host='0.0.0.0', access_log=False)


@app.get('/test/logging')
def log_check():
    logger.info('Logger is working')
    return 'Logger is working'


@app.get('/health')
def health_check():
    return {'STATUS": "UP'}


if __name__ == '__main__':
    main()
