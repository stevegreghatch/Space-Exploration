import logging
import requests
import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.main.service.dataService import programs, missions_by_program, astronauts_by_mission

env_vars = dotenv_values(".env")
NASA_API_KEY = env_vars.get('NASA_API_KEY')
NASA_API_URL = "https://images-api.nasa.gov/search?"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) to allow communication with React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (you may restrict this in production)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get('/nasa/images')
def get_images(query: str):
    logger.info('request received to get nasa images')
    api_key = env_vars.get('NASA_API_KEY')
    if not api_key:
        logger.error("NASA API key not found in environment variables.")
        raise HTTPException(status_code=500, detail="NASA API key not found")
    try:
        response = requests.get(NASA_API_URL, params={'q': query})
        response.raise_for_status()
        data = response.json()
        image_urls = []
        for item in data.get('collection', {}).get('items', []):
            for link in item.get('links', []):
                if 'href' in link:
                    image_urls.append(link['href'])
        return image_urls
    except Exception as e:
        logger.error(f"Error fetching images from NASA API: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch images from NASA API")


def main():
    logger.info('Logger configured')
    logger.info('Starting FastAPI application')
    uvicorn.run(app, port=8080, host='0.0.0.0', access_log=False)


# @app.get('/test/logging')
# def log_check():
#     logger.info('Logger is working')
#     return 'Logger is working'
#
#
# @app.get('/health')
# def health_check():
#     return {'STATUS": "UP'}


@app.get('/programs')
async def get_programs():
    logger.info('received request to get programs')
    return await programs()


@app.get('/missions/{program}')
async def get_missions_by_program(program: str):
    try:
        missions = await missions_by_program(program)
        return missions
    except Exception as e:
        logger.error(f"An error occurred while fetching missions for program {program}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get('/astronauts/{mission}')
async def get_astronauts_by_mission(mission: str):
    try:
        astronauts = await astronauts_by_mission(mission)
        return astronauts
    except Exception as e:
        logger.error(f"An error occurred while fetching astronauts for mission {mission}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == '__main__':
    main()
