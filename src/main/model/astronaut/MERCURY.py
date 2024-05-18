from enum import Enum


class AstronautName(str, Enum):
    ALAN_SHEPARD = "ALAN_SHEPARD"
    DEKE_SLAYTON = "DEKE_SLAYTON"
    GORDON_COOPER = "GORDON_COOPER"
    GUS_GRISSOM = "GUS_GRISSOM"
    JOHN_GLENN = "JOHN_GLENN"
    SCOTT_CARPENTER = "SCOTT_CARPENTER"
    WALLY_SCHIRRA = "WALLY_SCHIRRA"


# Example usage:
if __name__ == "__main__":
    print(AstronautName.GUS_GRISSOM.value)
