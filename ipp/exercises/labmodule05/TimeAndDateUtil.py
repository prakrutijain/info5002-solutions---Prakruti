

import datetime
import time

class TimeAndDateUtil():

    @classmethod
    def getCurrentLocalDateInMillis(cls):
        # time.time() returns seconds, so we multiply by 1000 for milliseconds
        current_millis = int(time.time() * 1000)
        return current_millis

    @classmethod
    def getCurrentIso8601LocalDate(cls, ignoreMillis: bool = True):
        # We use 'cls' to call other class methods

        current_date = datetime.datetime.fromtimestamp(cls.getCurrentLocalDateInMillis() / 1000)
        
        if ignoreMillis:
            current_date = current_date.replace(microsecond=0)
        
        return current_date.isoformat()

    @classmethod
    def getIso8601DateFromMillis(cls, millis: int = 0, ignoreMillis: bool = True):
        
        # Step 1: Validation - ensure millis is not negative
        if millis < 0:
            return "Invalid input: milliseconds must be 0 or greater"

        # Step 2: Convert milliseconds back to seconds for datetime
        seconds = millis / 1000.0
        date_obj = datetime.datetime.fromtimestamp(seconds)

        # Step 3: Handle microsecond stripping if requested
        if ignoreMillis:
            date_obj = date_obj.replace(microsecond=0)

        # Step 4: Return the ISO 8601 string
        return date_obj.isoformat()
    
   