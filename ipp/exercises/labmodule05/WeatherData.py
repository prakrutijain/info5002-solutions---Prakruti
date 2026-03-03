
from dataclasses import dataclass, field
from typing import List, Optional

# Import your custom modules
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherInfoContainer import WindData, VisibilityData, CloudLayerData

@dataclass
class WeatherData:
    # Basic attributes with simple defaults
    source: str = ""
    url: str = ""
    description: str = ""
    
    # Automatically get the current time when an object is created
    timestamp: str = field(default_factory=TimeAndDateUtil.getCurrentIso8601LocalDate)
    
    temperature: float = 0.0
    humidity: float = 0.0
    pressure: float = 0.0
    windspeed: float = 0.0
    conditions: str = 'N/A'
    icon: Optional[str] = None

    # Complex attributes (Classes inside this class)
    # We use default_factory so each WeatherData object gets its own NEW instance
    location: LocationData = field(default_factory=LocationData)
    wind: WindData = field(default_factory=WindData)
    visibility: VisibilityData = field(default_factory=VisibilityData)
    
    # An empty list for multiple cloud layers
    cloudLayers: List[CloudLayerData] = field(default_factory=list)

from dataclasses import dataclass, field
from typing import List, Optional

# Import your custom modules
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherInfoContainer import WindData, VisibilityData, CloudLayerData

@dataclass
class WeatherData:
    # Basic attributes
    source: str = ""
    url: str = ""
    description: str = ""
    
    # default_factory calls the function for every new object
    timestamp: str = field(default_factory=TimeAndDateUtil.getCurrentIso8601LocalDate)
    
    temperature: float = 0.0
    humidity: float = 0.0
    pressure: float = 0.0
    dewpoint: float = 0.0 # Added to match common lab requirements
    windspeed: float = 0.0
    conditions: str = 'N/A'
    icon: Optional[str] = None

    # Complex attributes
    location: LocationData = field(default_factory=LocationData)
    wind: WindData = field(default_factory=WindData)
    visibility: VisibilityData = field(default_factory=VisibilityData)
    
    # Empty list for cloud layers
    cloudLayers: List[CloudLayerData] = field(default_factory=list)