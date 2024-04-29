from typing import Callable, List
from nicegui import ui, events, app

class Manager(object):
    _status: str
    host: str

    listeners: List[Callable[[str], None]] = []

    def __init__(self) -> None:
        self._status = "UNBOUND"

    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, value: str) -> None:
        self._status = value
        for listener in self.listeners:
            listener(self.status)

    def connect(self, mqtt_host, mqtt_port, mqtt_username, mqtt_password):
        self.host = mqtt_host
        self.status = "BOUND"

    def restart(self):
        self.status = "UNBOUND"

    def add_bind_status_listener(self, listener):
        self.listeners.append(listener)


manager = Manager()

@ui.refreshable
def connection_state() -> None:
    ui.label(f"Status: {manager.status}")
    if manager.status == "UNBOUND":
        connection = {
            "mqtt_host": "rabbitmq",
            "mqtt_port": 1883,
            "mqtt_username": "vhost1:user1",
            "mqtt_password": "password1",
        }
        ui.input(label="MQTT Host").bind_value(
            connection, "mqtt_host"
        )  # dev-diab-api.flyfreely.io
        ui.input(label="MQTT Port").bind_value(connection, "mqtt_port")
        ui.input(label="MQTT Username").bind_value(
            connection, "mqtt_username"
        )
        ui.input(label="MQTT Password").bind_value(
            connection, "mqtt_password"
        )
        ui.button(
            "Connect",
            on_click=lambda: manager.connect(
                connection["mqtt_host"],
                connection["mqtt_port"],
                connection["mqtt_username"],
                connection["mqtt_password"],
            ),
        )
    if manager.status == "BOUND":
        ui.label(f"Host: {manager.host}")
    if manager.status != "UNBOUND":
        ui.button("Restart", on_click=lambda: manager.restart())


@ui.page("/")
def main():
    connection_state()
    manager.add_bind_status_listener(lambda x: connection_state.refresh())
