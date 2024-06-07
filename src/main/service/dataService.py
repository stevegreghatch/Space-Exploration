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


async def programs():
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.programs.select(
                        ds.ProgramType.program,
                        ds.ProgramType.missions,
                        ds.ProgramType.image_url
                    )
                )
            )
            program_data = await session.execute(query)
            return program_data
    except Exception as exception:
        raise exception


async def missions():
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.missions.select(
                        ds.MissionType.mission,
                        ds.MissionType.astronauts,
                        ds.MissionType.program,
                        ds.MissionType.call_sign,
                        ds.MissionType.image_url,
                        ds.MissionType.launch_date_utc,
                        ds.MissionType.launch_mass_lbs,
                        ds.MissionType.launch_site,
                        ds.MissionType.launch_site_coord,
                        ds.MissionType.launch_vehicle,
                        ds.MissionType.orbits,
                        ds.MissionType.apogee_nmi,
                        ds.MissionType.perigee_nmi,
                        ds.MissionType.landing_date_utc,
                        ds.MissionType.landing_site,
                        ds.MissionType.landing_site_coord,
                        ds.MissionType.recovery_ship,
                        ds.MissionType.duration.select(
                            ds.DurationType.days,
                            ds.DurationType.hours,
                            ds.DurationType.minutes,
                            ds.DurationType.seconds
                        )
                    )
                )
            )
            mission_data = await session.execute(query)
            return mission_data
    except Exception as exception:
        raise exception


async def astronauts():
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.astronauts.select(
                        ds.AstronautType.astronaut_first_name,
                        ds.AstronautType.astronaut_last_name,
                        ds.AstronautType.image_url,
                        ds.AstronautType.missions
                    )
                )
            )
            astronaut_data = await session.execute(query)
            return astronaut_data
    except Exception as exception:
        raise exception


async def missions_by_program(program):
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.missions_by_program(program=program).select(
                        ds.MissionType.mission,
                        ds.MissionType.astronauts,
                        ds.MissionType.program,
                        ds.MissionType.call_sign,
                        ds.MissionType.image_url,
                        ds.MissionType.launch_date_utc,
                        ds.MissionType.launch_mass_lbs,
                        ds.MissionType.launch_site,
                        ds.MissionType.launch_site_coord,
                        ds.MissionType.launch_vehicle,
                        ds.MissionType.orbits,
                        ds.MissionType.apogee_nmi,
                        ds.MissionType.perigee_nmi,
                        ds.MissionType.landing_date_utc,
                        ds.MissionType.landing_site,
                        ds.MissionType.landing_site_coord,
                        ds.MissionType.recovery_ship,
                        ds.MissionType.duration.select(
                            ds.DurationType.days,
                            ds.DurationType.hours,
                            ds.DurationType.minutes,
                            ds.DurationType.seconds
                        )
                    )
                )
            )
            mission_data = await session.execute(query)
            return mission_data
    except Exception as exception:
        raise exception


async def astronauts_by_mission(mission):
    try:
        transport = AIOHTTPTransport(url=GRAPHQL_URL)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        async with client as session:
            ds = DSLSchema(client.schema)
            query = dsl_gql(
                DSLQuery(
                    ds.Query.astronauts_by_mission(mission=mission).select(
                        ds.AstronautType.astronaut_first_name,
                        ds.AstronautType.astronaut_last_name,
                        ds.AstronautType.image_url,
                        ds.AstronautType.missions
                    )
                )
            )
            astronaut_data = await session.execute(query)
            return astronaut_data
    except Exception as exception:
        raise exception


# if __name__ == '__main__':
#     asyncio.run(programs())
