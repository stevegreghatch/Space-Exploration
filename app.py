import logging
import requests
import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.main.service.dataService import programs, missions, astronauts, missions_by_program, astronauts_by_mission
from src.main.service.mappingService2D import generate_map_data

env_vars = dotenv_values(".env")
NASA_API_KEY = env_vars.get('NASA_API_KEY')
NASA_API_URL = "https://images-api.nasa.gov/search?"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        response = requests.get(NASA_API_URL, params={'q': query, 'media_type': 'image'})
        response.raise_for_status()
        data = response.json()

        images_info = []

        for item in data.get('collection', {}).get('items', []):
            image_data = {
                'title': None,
                'description': None,
                'link': None
            }

            if item_data := item.get('data', []):
                image_data['title'] = item_data[0].get('title')
                image_data['description'] = item_data[0].get('description')

            for link in item.get('links', []):
                if link.get('rel') == 'preview' and link.get('href'):
                    image_data['link'] = link['href']

            images_info.append(image_data)

        return images_info

    except Exception as e:
        logger.error(f"Error fetching images from NASA API: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch images from NASA API")


@app.get('/map/{mission_name}', response_class=JSONResponse)
async def get_map(mission_name: str):
    try:
        logger.info(f'Received request to generate map for mission: {mission_name}')
        all_missions = await missions()
        mission_data = next((m for m in all_missions['missions'] if m['mission'] == mission_name), None)
        if not mission_data:
            raise HTTPException(status_code=404, detail="Mission not found")

        launch_site_dms = mission_data['launchSiteCoord']
        landing_site_dms = mission_data['landingSiteCoord']

        fig = generate_map_data(mission_name, launch_site_dms, landing_site_dms)

        fig_json = fig.to_dict()

        return JSONResponse(content=fig_json)
    except Exception as e:
        logger.error(f"Error generating map: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate map")


@app.get('/programs')
async def get_programs():
    logger.info('received request to get all programs')
    return await programs()


@app.get('/missions')
async def get_missions():
    logger.info('received request to get all missions')
    return await missions()


@app.get('/astronauts')
async def get_astronauts():
    logger.info('received request to get all astronauts')
    return await astronauts()


@app.get('/missions/{program}')
async def get_missions_by_program(program: str):
    try:
        return await missions_by_program(program)
    except Exception as e:
        logger.error(f"An error occurred while fetching missions for program {program}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get('/astronauts/{mission}')
async def get_astronauts_by_mission(mission: str):
    try:
        return await astronauts_by_mission(mission)
    except Exception as e:
        logger.error(f"An error occurred while fetching astronauts for mission {mission}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get('/space-exploration/test')
async def get_test_response():
    return True


def main():
    logger.info('Logger configured')
    logger.info('Starting FastAPI application')
    uvicorn.run(app, port=8080, host='0.0.0.0', access_log=False)


if __name__ == '__main__':
    main()
