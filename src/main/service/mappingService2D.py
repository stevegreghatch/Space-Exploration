import plotly.graph_objects as go
import re


def dms_to_dd(dms):
    # Check if the input is in decimal degrees with direction
    match_decimal = re.match(r"(-?\d+(\.\d+)?)[°\s]*([NSEW])", dms)
    if match_decimal:
        dd, _, direction = match_decimal.groups()
        dd = float(dd)
        if direction in ['S', 'W']:
            dd *= -1
        return dd

    # Regex to capture degrees, minutes, seconds, and direction
    match_dms = re.match(r"(\d+)[°\s]+(\d+)?[′\s]*([\d.]*)[″\s]*([NSEW])", dms)
    if match_dms:
        d, m, s, direction = match_dms.groups()
        d = float(d) if d else 0
        m = float(m) if m else 0
        s = float(s) if s else 0
        dd = d + m / 60 + s / 3600
        if direction in ['S', 'W']:
            dd *= -1
        return dd
    else:
        raise ValueError(f"Invalid DMS coordinate: {dms}")


def generate_map_data(mission_name, launch_site_dms, landing_site_dms):
    launch_site_parts = launch_site_dms.split()
    landing_site_parts = landing_site_dms.split()

    launch_site_coord_dd = (dms_to_dd(launch_site_parts[0]), dms_to_dd(launch_site_parts[1]))
    landing_site_coord_dd = (dms_to_dd(landing_site_parts[0]), dms_to_dd(landing_site_parts[1]))

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=[launch_site_coord_dd[1]],
        lat=[launch_site_coord_dd[0]],
        text="Launch Site",
        mode='markers',
        marker=dict(size=10, color='blue', symbol='circle'),
        name="launch site"
    ))

    fig.add_trace(go.Scattergeo(
        lon=[landing_site_coord_dd[1]],
        lat=[landing_site_coord_dd[0]],
        text="Landing Site",
        mode='markers',
        marker=dict(size=10, color='red', symbol='circle'),
        name="landing site"
    ))

    fig.update_layout(
        title=f'{mission_name} Mission',
        geo=dict(
            projection_type='orthographic',
            showland=True
        )
    )

    return fig
