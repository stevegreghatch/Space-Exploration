import asyncio
import logging
from gql import Client
from gql.dsl import DSLSchema, DSLQuery, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

logging.getLogger('gql.transport.aiohttp').setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

GRAPHQL_URL = 'http://localhost:8081/graphql'


async def astronauts():
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.astronauts.select(
                        ds.AstronautType.first_name,
                        ds.AstronautType.last_name,
                        ds.AstronautType.programs,
                        ds.AstronautType.image_url,
                        ds.AstronautType.missions
                    )
                )
            )
            astronauts_data = await session.execute(query)
            return astronauts_data
    except Exception as exception:
        raise exception


async def astronauts_by_program(program: str):
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.astronautsByProgram(
                        program=program
                    ).select(
                        ds.AstronautType.first_name,
                        ds.AstronautType.last_name,
                        ds.AstronautType.programs,
                        ds.AstronautType.image_url,
                        ds.AstronautType.missions
                    )
                )
            )
            astronauts_data = await session.execute(query)
            return astronauts_data
    except Exception as exception:
        logger.error(f"An error occurred: {exception}")
        raise exception


async def project_mercury():
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.project_mercury.select(
                        ds.MissionType.astronaut,
                        ds.MissionType.apogeeMi,
                        ds.MissionType.callSign,
                        ds.MissionType.duration.select(
                            ds.DurationType.days,
                            ds.DurationType.hours,
                            ds.DurationType.minutes,
                            ds.DurationType.seconds,
                        ),
                        ds.MissionType.launchSite,
                        ds.MissionType.launchTime,
                        ds.MissionType.missMi,
                        ds.MissionType.mission,
                        ds.MissionType.orbits,
                        ds.MissionType.perigeeMi,
                        ds.MissionType.spacecraftNumber,
                        ds.MissionType.velocityMaxMph
                    )
                )
            )
            mission_data = await session.execute(query)
            return mission_data
    except Exception as exception:
        raise exception


async def project_mercury_by_call_sign(call_sign: str):
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.project_mercury_by_call_sign(
                        where={"call_sign": call_sign}
                    ).select(
                        ds.MissionType.astronaut,
                        ds.MissionType.apogeeMi,
                        ds.MissionType.callSign,
                        ds.MissionType.duration.select(
                            ds.DurationType.days,
                            ds.DurationType.hours,
                            ds.DurationType.minutes,
                            ds.DurationType.seconds,
                        ),
                        ds.MissionType.launchSite,
                        ds.MissionType.launchTime,
                        ds.MissionType.missMi,
                        ds.MissionType.mission,
                        ds.MissionType.orbits,
                        ds.MissionType.perigeeMi,
                        ds.MissionType.spacecraftNumber,
                        ds.MissionType.velocityMaxMph
                    )
                )
            )
            mission_data = await session.execute(query)
            return mission_data
    except Exception as exception:
        raise exception


if __name__ == '__main__':
    asyncio.run(astronauts_by_program('Mercury'))
    # asyncio.run(astronauts())
    # asyncio.run(all_data_project_mercury())
    # asyncio.run(mission_project_mercury_call_sign('Liberty Bell 7'))
