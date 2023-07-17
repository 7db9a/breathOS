import pytest
from datetime import datetime
from your_module import AppCollection  # Replace with your actual module path

class TestAppCollection:
    @pytest.fixture
    def app_collection(self):
        return AppCollection()

    def test_should_roll_back_app_version(self, app_collection):
        # Assuming the AppID of an existing app in the collection is known
        known_app_id = "some_known_app_id"

        # Specify the date and time to roll back to
        rollback_date = datetime(2023, 1, 1, 10, 30)  # Example date

        # Perform the rollback
        rollback_result = app_collection.rollback_app(known_app_id, rollback_date)

        assert rollback_result is True, "The rollback operation was not successful."

        # Confirm the current version is as expected
        current_version = app_collection.get_app_current_version(known_app_id)

        # We should have some mechanism to know the expected version corresponding to the rollback date.
        # For this test, let's assume there is a method 'get_version_by_date' in the 'AppCollection' class.
        expected_version = app_collection.get_version_by_date(known_app_id, rollback_date)

        assert current_version == expected_version, "The rolled back version does not match the expected version."