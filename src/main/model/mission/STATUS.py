from enum import Enum


class MissionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"


# Example usage:
if __name__ == "__main__":
    print(MissionStatus.SUCCESS.value)
