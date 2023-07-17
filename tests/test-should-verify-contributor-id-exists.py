import pytest
from your_module import AppCollection  # Replace with your actual module path

class TestAppCollection:
    @pytest.fixture
    def app_collection(self):
        # Setup code here, if needed
        return AppCollection()

    @pytest.mark.asyncio
    async def test_should_verify_contributorID_exists(self, app_collection):
        # Here we're assuming that there's an `add_app` method which adds an app to the internal list
        app_data = {
            "gitURL": "<git_url>"
        }

        # Test if exception is raised when the "ContributorID" field is missing
        with pytest.raises(ValueError):
            await app_collection.add_app(app_data)