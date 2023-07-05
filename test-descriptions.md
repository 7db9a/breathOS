1. `test_should_add_app_from_file`: This test ensures that the `add_app_from_file` function correctly reads data from the provided file and adds a corresponding App instance to the AppCollection's list of apps. It checks for the presence of the mandatory ContributorID field.

2. `test_should_update_apps`: This test verifies that the `update_apps` function correctly iterates over the AppCollection's list of apps, pulls the latest changes from the corresponding git repositories, and attempts to reinstall them.

3. `test_should_install_app`: This test checks that the `install_app` function successfully clones the app's git repository if it hasn't already been cloned, finds the Dockerfile in the appropriate directory, and uses it to build a new Docker image. It also verifies the presence and correct placement of the `app.manager` file and that Docker images can be built using it.

4. `test_should_verify_contributorID_exists`: This test ensures that the `ContributorID` field exists in the `app.collection` file when adding an app. If the `ContributorID` field does not exist, the test should result in an error or exception.

5. `test_should_generate_correct_appID_hash`: This test verifies that the `App` class correctly generates a hash for the `AppID` based on the `ContributorID` and `gitURL`. The test compares the generated hash against an expected hash value to verify the correctness of the hashing function.

6. `test_should_rehash_appID_on_changes`: This test checks that when changes are made to the `app.collection` file, a new `AppID` is generated. This is important as each distinct state of the application (defined by its `app.collection` file) should have a unique `AppID`.

7. `test_should_verify_docker_compose_exists_and_builds_image`: This test checks the presence and correct placement of the `app.manager` file (a Docker Compose file), and verifies that Docker images can be built using it. It also checks for the presence of the `PORT_HOST` and `PORT_CONTAINER` placeholders in the `app.manager` file for potential port mapping.

8. `test_should_assign_non_colliding_ports`: This test ensures that when an app is added to the AppCollection, unique port numbers for `PORT_HOST` and `PORT_CONTAINER` are assigned by the AppCollection, ensuring that these ports do not collide with ports assigned to other apps in the collection.

9. `test_should_display_app_versions_with_date_time`: This test ensures that the application can correctly display the date and time of every version of an app from the commit history in the git repository. The displayed information should match the actual commit history of the repository.

10. `test_should_roll_back_app_version`: This test checks if the application can correctly roll back an app to a previous version by passing a date and time as arguments. The rolled back version should match the state of the app at the specified date and time according to the commit history.

11. `test_should_roll_forward_app_version`: Similar to the roll back test, this test verifies if the application can roll forward an app to a newer version by passing a date and time as arguments. The updated version should match the state of the app at the specified date and time according to the commit history.
