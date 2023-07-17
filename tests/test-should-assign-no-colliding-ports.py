import pytest
from your_module import AppCollection  # Replace with your actual module path

class TestAppCollection:
    @pytest.fixture
    def app_collection(self):
        return AppCollection()

    def test_should_assign_non_colliding_ports(self, app_collection):
        apps = ["app1", "app2", "app3"]  # list of mock apps
        assigned_ports = []

        for app in apps:
            app_collection.add_app(app)  # Assumes add_app is a method to add an app to the collection

            # Get the assigned ports for this app
            # Assumes get_app_ports is a method to get assigned ports for an app
            port_host, port_container = app_collection.get_app_ports(app)  

            assert (port_host, port_container) not in assigned_ports, "Port collision detected."

            assigned_ports.append((port_host, port_container))