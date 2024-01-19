import pytest

from paralympics.models import Region, Admin, Event


@pytest.fixture(scope='function')
def event():
    e = Event(event_type="winter", year=2032, country="South Africa", host="Cape Town", noc="RSA",
    start="01/01/2032", end="14/01/2032", disabilities_included="", countries=0, events=15,
    sports=0, participants_m=0, participants_f=0, participants=0, highlights="")
    return e

def test_create_region_valid():
    """
    GIVEN valid data for a Region object
    WHEN the Region object is created
    THEN the code should have a 3 character code, region is a string
    and notes fields can be an empty string
    :return:
    """
    region = Region("CHN", "China")
    assert region.code == "CHN"
    assert region.region == "China"
    assert region.notes == ""


def test_invalid_code_raises_error():
    """
    GIVEN invalid data for the Region object code attribute, code="China"
    WHEN the Region object is created
    THEN a ValueException is raised
    """
    with pytest.raises(ValueError):
        Region("China", "China")


def test_create_admin_valid():
    """
    GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
    WHEN the Admin object 'admin' is created
    THEN admin.email should equal 'test@test.com' and admin._password should be longer than 'testpassword' as it is a hashed value
    """
    admin = Admin("test@test.com", "testpassword")
    assert admin.email == "test@test.com"
    assert len(admin._password) > len("testpassword")

def test_inavlid_event_type_raises_error():
    """
    GIVEN invalid data for the Event object event_type attribute, event_type="autumn"
    WHEN the Event object is created
    THEN a ValueException is raised
    """
    with pytest.raises(ValueError):
        Event(event_type="autumn",
                year=2032,
                country="South Africa",
                host="Cape Town",
                noc="RSA",
                start="01/01/2032",
                end="14/01/2032",)

def test_event_created_with_valid_data(event):
    """
    GIVEN valid data for the Event object
    WHEN the Event object called event is created
    THEN check the event attributes are correct
    """
    assert event.event_type == "winter"
    assert event.year == 2032
    assert event.country == "South Africa"
    assert event.host == "Cape Town"
    assert event.noc == "RSA"
    assert event.start == "01/01/2032"
    assert event.end == "14/01/2032"
    assert event.disabilities_included == ""
    assert event.countries == 0
    assert event.events == 15
    assert event.sports == 0
    assert event.participants_m == 0
    assert event.participants_f == 0
    assert event.participants == 0
    assert event.highlights == ""   
        

def test_admin_check_password():
    """
    GIVEN a valid Admin object with a hashed password
    WHEN check_password method is called with the correct password
    THEN it should return True
    """
    admin = Admin("test@test.com", "testpassword")
    assert admin.check_password("testpassword") is True


def test_admin_check_password_incorrect():
    """
    GIVEN a valid Admin object with a hashed password
    WHEN check_password method is called with an incorrect password
    THEN it should return False
    """
    admin = Admin("test@test.com", "testpassword")
    assert admin.check_password("incorrectpassword") is False


def test_admin_change_password():
    """
    GIVEN a valid Admin object with a hashed password
    WHEN change_password method is called with the correct old password and a new password
    THEN the password should be successfully changed
    """
    admin = Admin("test@test.com", "testpassword")
    admin.change_password("testpassword", "newpassword")
    assert admin.check_password("newpassword") is True


def test_admin_change_password_incorrect_old_password():
    """
    GIVEN a valid Admin object with a hashed password
    WHEN change_password method is called with an incorrect old password and a new password
    THEN it should raise a ValueError
    """
    admin = Admin("test@test.com", "testpassword")
    with pytest.raises(ValueError):
        admin.change_password("incorrectpassword", "newpassword")
        