import pytest


@pytest.fixture(scope="session")
def mock_dependency():
    dependency: list[int] = [3]
    yield dependency
    print("Finished test with dependency at final state", dependency)
    del dependency


class TestSomething:
    def test_add(self, mock_dependency: list[int]):
        mock_dependency[0] += 1
        assert (
            mock_dependency[0] == 4
        ), "Dependency Injection is not working as expected"

    def test_state(self, mock_dependency: list[int]):
        assert (
            mock_dependency[0] == 4
        ), "Dependency Injection is not working as expected"


class TestSomething2:
    def test_state(self, mock_dependency: list[int]):
        assert (
            mock_dependency[0] == 4
        ), "Dependency Injection is not working as expected"
