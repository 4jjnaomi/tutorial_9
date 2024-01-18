import hashlib


class Region:
    """ Represents a region definition from the National Olympic Committee
    """

    def __init__(self, code, region, notes=""):
        self.code = code
        self.region = region
        self.notes = notes

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        # Only sets the value if it is 3 chars and uppercase, otherwise raises value error
        val_upper = value.upper()
        if len(val_upper) == 3:
            self._code = val_upper
        else:
            raise ValueError(f"NOC code {value} must be exactly 3 characters e.g. 'CHN' for China")


class Event:
    """ Represents the details for one paralympic event
    """

    def __init__(self, event_type, year: int, country: str, host: str, noc, start, end, duration=0,
                 disabilities_included="", countries=0, events=0, sports=0, participants_m=0, participants_f=0,
                 participants=0, highlights=""):
        self.event_type = event_type
        self.year = year
        self.country = country
        self.host = host
        self.noc = noc
        self.start = start
        self.end = end
        self.duration = duration
        self.disabilities_included = disabilities_included
        self.countries = countries
        self.events = events
        self.sports = sports
        self.participants_m = participants_m
        self.participants_f = participants_f
        self.participants = participants
        self.highlights = highlights

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """
        Converts the event type to lower case and checks it is either summer or winter
        If valid, set the event_type attribute to the lowercase value
        Otherwise raise a ValueError
        :param value:
        :raises: ValueError
        """
        val_lower = value.lower()
        if val_lower in {"winter", "summer"}:
            self._event_type = val_lower
        else:
            raise ValueError(f"Event type {value} must be either 'summer' or 'winter'.")

    @property
    def noc(self):
        return self._noc

    @noc.setter
    def noc(self, value):
        # Only sets the value if it is 3 chars and uppercase, otherwise raises value error
        val_upper = value.upper()
        if len(val_upper) == 3:
            self._noc = val_upper
        else:
            raise ValueError(f"NOC code {value} must be exactly 3 characters e.g. 'GER'")


class Admin:
    """
    User class with email address, password and stores the pashword as a hash
    """

    def __init__(self, email, password):
        self.email = email
        self._password = self._hash_password(password)

    @staticmethod
    def _hash_password(password):
        """
        Hashes the password using the sha256 algorithm
        :param password:
        :return: hashed password
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def check_password(self, password):
        """
        Checks if the password is correct by hashing the password and comparing to the stored hash
        :param password:
        :return: True if the password is correct, otherwise False
        """
        return self._password == self._hash_password(password)

    def change_password(self, old_password, new_password):
        """
        Checks if the old password is correct and if so, changes the password to the new password
        :param old_password:
        :param new_password:
        :return: ValueError if the old password is incorrect
        """
        if self.check_password(old_password):
            self._password = self._hash_password(new_password)
        else:
            raise ValueError(f"Current password {old_password} is incorrect")
