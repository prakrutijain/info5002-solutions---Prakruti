class WindData:
    """Stores information about wind speed and direction."""
    def __init__(self):
        # Speed in Kilometers per hour
        self.speedKph = 0.0
        # Maximum 'gust' speed in Kph
        self.gustKph = 0.0
        # Wind direction (0-360 degrees)
        self.directionDegrees = 0.0

class VisibilityData:
    """Stores how far you can see in meters."""
    def __init__(self):
        # Distance in meters
        self.meters = 0.0

class CloudLayerData:
    """Stores the density and altitude of cloud layers."""
    def __init__(self):
        # Amount of cloud cover (often 0.0 to 1.0 or a percentage)
        self.amount = 0.0
        # How high the clouds start in meters
        self.baseMeters = 0.0

