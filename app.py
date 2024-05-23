import logging
import requests
import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from src.main.service.dataService import astronauts, astronauts_by_program

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


@app.get('/test/logging')
def log_check():
    logger.info('Logger is working')
    return 'Logger is working'


@app.get('/health')
def health_check():
    return {'STATUS": "UP'}


@app.get('/astronauts')
async def get_astronauts():
    logger.info('request received to get astronauts')
    return await astronauts()


@app.get('/astronauts/program')
async def get_astronauts_by_program(program: str) -> List[Dict]:
    try:
        logger.info(f'Request received to get astronauts for program: {program}')
        astronaut_data = await astronauts_by_program(program)
        return astronaut_data.get('astronautsByProgram', [])  # Assuming 'astronautsByProgram' is the key containing the list of astronaut data
    except Exception as e:
        logger.error(f"An error occurred while fetching astronauts: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch astronauts")



if __name__ == '__main__':
    main()
