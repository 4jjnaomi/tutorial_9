import pytest

from paralympics.models import Region, Admin, Event


def test_create_region_valid():
    """
    GIVEN valid data for a Region object
    WHEN the Region object is created
    THEN the code should have a 3 character code, region is a string and notes fields can be an empty string
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
        
        
