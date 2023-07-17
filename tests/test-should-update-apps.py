import pytest
from git import Repo
from subprocess import call
from your_module import AppCollection  # Replace with your actual module path


class TestAppCollection:
    @pytest.fixture
    def app_collection(self):
        # Setup code here, if needed
        return AppCollection()

    @pytest.mark.asyncio
    async def test_should_update_apps(self, app_collection):
        apps = await app_collection.get_apps()

        for app in apps:
            # Assuming each 'app' is a dict with 'ContributorID' and 'gitURL' keys
            git_url = app['gitURL']

            # Clone (or pull) the git repo into a local directory
            try:
                repo = Repo.clone_from(git_url, '/tmp/repo')
            except:
                repo = Repo('/tmp/repo')
                o = repo.remotes.origin
                o.pull()

            # Get the commit SHA before the update
            before_commit_sha = repo.head.object.hexsha

            # Attempt to reinstall (update) the app
            await app_collection.update_app(app)

            # Check if the repo has new commits
            after_commit_sha = repo.head.object.hexsha

            assert before_commit_sha != after_commit_sha, \
                f"App from {git_url} was not updated correctly"

            # Assuming the update of the app triggers a rebuild and reinstall
            # Here, we're assuming a function that mimics such an action
            rebuild_return_code = call(['docker', 'build', '-t', app['ContributorID'], '.'])

            assert rebuild_return_code == 0, \
                f"App from {git_url} could not be reinstalled correctly"

            # Cleanup the cloned repo
            call(['rm', '-rf', '/tmp/repo'])