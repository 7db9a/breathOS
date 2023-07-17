import json
import pytest
from your_module import AppCollection  # Replace with your actual module path

class TestAppCollection:
    @pytest.fixture
    def app_collection(self):
        return AppCollection()

    @pytest.fixture
    def app_file(self, tmp_path):
        app_data = {
            "ContributorID": "test_id",
            "gitURL": "test_git_url"
        }

        app_file_path = tmp_path / "app.collection"
        app_file_path.write_text(json.dumps(app_data))
        return str(app_file_path)

    def test_should_get_app_port(self, app_collection, app_file):
        app_collection.add_app_from_file(app_file)  # Assumes add_app_from_file is a method to add an app from a file

        # Get the last added app
        # Assumes get_last_app is a method to get the last added app
        last_app = app_collection.get_last_app()

        assert last_app is not None, "No app was added."

        # Assumes each app has a unique AppID
        app_id = last_app["AppID"]

        # Assumes get_app_port is a method to get an app's port by its AppID
        port = app_collection.get_app_port(app_id)

        assert port is not None, "No port was assigned."
        assert isinstance(port, int), "The port should be an integer."