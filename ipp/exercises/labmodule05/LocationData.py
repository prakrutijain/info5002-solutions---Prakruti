

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil


class LocationData():
    """
    A data container class to hold geographical information.
    """

    def __init__(self):
        # 'self' refers to the specific instance of the location being created.
        # We use type hints (like : str) to show what kind of data belongs here.
        
        self.name: str = ""       # Example: "Mount Everest"
        self.nameID: str = ""     # Example: "ID_12345"
        self.city: str = ""       # Example: "Kathmandu"
        self.region: str = ""     # Example: "Sagarmatha"
        self.country: str = ""    # Example: "Nepal"
        
        # Coordinates and height use floats (decimals) for precision
        self.latitude: float = 0.0
        self.longitude: float = 0.0
        self.elevation: float = 0.0
        
        self.timestamp: str  = TimeAndDateUtil.getCurrentIso8601LocalDate()
