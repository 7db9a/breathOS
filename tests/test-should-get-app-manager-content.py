import pytest
import json
from your_module import App  # Replace with your actual module path

class TestApp:
    @pytest.fixture
    def app(self):
        # Setup code here, if needed
        return App()

    def test_should_rehash_appID_on_changes(self, app):
        initial_app_collection = json.dumps({
            "ContributorID": "<initial_contributor_id>",
            "gitURL": "<initial_git_url>"
        })
        updated_app_collection = json.dumps({
            "ContributorID": "<updated_contributor_id>",
            "gitURL": "<updated_git_url>"
        })

        # Generate initial AppID
        initial_appID = app.update_app_collection(initial_app_collection)

        # Update app.collection and generate new AppID
        updated_appID = app.update_app_collection(updated_app_collection)

        # Check that the AppID has changed after the update
        assert initial_appID != updated_appID