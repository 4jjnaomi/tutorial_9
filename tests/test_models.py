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
