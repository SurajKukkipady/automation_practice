import pytest

@pytest.fixture(scope="session")
def user(request):
    return request.param