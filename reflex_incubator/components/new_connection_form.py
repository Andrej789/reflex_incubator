# Python modules
from typing import Literal, Optional

# 3rd party modules
import reflex as rx
from pydantic import BaseModel


class ConnectionDefinitionModel(BaseModel):
    connection_name: Optional[str] = None
    username: Optional[str] = None
    password:Optional[str] = None
    hostname: Optional[str] = None
    port: str = "1521"
    type: Literal["SID", "SN"] = "SID"
    sid: Optional[str] = None
    service_name: Optional[str] = None

    def is_valid(self) -> bool:
        if not self.connection_name:
            return False
        if not self.username:
            return False
        if not self.password:
            return False
        if not self.hostname:
            return False
        if self.type == 'SID' and not self.sid:
            return False
        if self.type == 'SN' and not self.service_name:
            return False
        return True


class NewConnectionFormState(rx.State):
    is_disabled: bool = True  # If TRUE, dialog submit button is disabled otherwise enabled.
    connection_def: ConnectionDefinitionModel = ConnectionDefinitionModel()
    type_options: list[dict[str, str]] = [
        {"key": "SID", "label": "SID"},
        {"key": "SN", "label": "Service Name"},
    ]
    _cnt: int = 0  # FIXME: Remove - for testing purposes only.
    
    @rx.event
    def handle_validation(self, value: str) -> None:
        if self.connection_def.is_valid():
            self.is_disabled = False
        else:
            self.is_disabled = True
        self._cnt+=1
        print(f"handle_validation {self._cnt}: {self.is_disabled}")
        print(self.connection_def)

    @rx.event
    def handle_submit(self, form_data: dict) -> None:
        self.connection_def = ConnectionDefinitionModel(**form_data)
        print(self.connection_def.connection_name)

    @rx.event
    def handle_type_select(self, value: str) -> None:
        for option in self.type_options:
            if option["key"] == value:
                self.connection_def.type = option["key"]
                break
    
    @rx.event
    def handle_open_change(self, value: bool) -> None:
        print(f"Dialog open state is {value}")


class NewConnectionForm():

    def create_v1(self) -> rx.Component:
        return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("plus", size=20),
                    rx.text("New Connection"),
                ),
            ),
            rx.dialog.content(
                rx.dialog.title("New Connection"),
                rx.dialog.description("Fill the form with connection's metadata"),
                rx.form(
                    rx.vstack(
                        # ===  Connection name  =======================================================
                        rx.vstack(
                            rx.text.strong(
                                "Connection Name",
                                rx.text.span(" *", color=rx.color("red", 9)),
                            ),
                            rx.input(
                                name="connection_name",
                                required=True,
                                on_blur=NewConnectionFormState.handle_validation,
                            ),
                            spacing="0",
                            width="100%",
                            align="stretch",
                        ),
                        # ===  Username  ==============================================================
                        rx.vstack(
                            rx.text.strong(
                                "Username",
                                rx.text.span(" *", color=rx.color("red", 9)),
                            ),
                            rx.input(
                                name="username",
                                required=True,
                                on_blur=NewConnectionFormState.handle_validation,
                            ),
                            spacing="0",
                            width="100%",
                            align="stretch",
                        ),
                        # ===  Password  ==============================================================
                        rx.vstack(
                            rx.text.strong(
                                "Password",
                                rx.text.span(" *", color=rx.color("red", 9)),
                            ),
                            rx.input(
                                name="password",
                                type="password",
                                required=True,
                                on_blur=NewConnectionFormState.handle_validation,
                            ),
                            spacing="0",
                            width="100%",
                            align="stretch",
                        ),
                        # ===  Hostname  ==============================================================
                        rx.vstack(
                            rx.text.strong(
                                "Hostname",
                                rx.text.span(" *", color=rx.color("red", 9)),
                            ),
                            rx.input(
                                name="hostname",
                                required=True,
                                on_blur=NewConnectionFormState.handle_validation,
                            ),
                            spacing="0",
                            width="100%",
                            align="stretch",
                        ),
                        # ===  Port  ==================================================================
                        rx.vstack(
                            rx.text.strong(
                                "Port"
                            ),
                            rx.input(
                                name="port",
                                default_value="1521",
                                required=True,
                                on_blur=NewConnectionFormState.handle_validation,
                            ),
                            spacing="0",
                            width="100%",
                            align="stretch",
                        ),
                        # ===  Type  ==================================================================
                        rx.hstack(
                            rx.vstack(
                                rx.text.strong(
                                    "Type"
                                ),
                                rx.select.root(
                                    rx.select.trigger(),
                                    rx.select.content(
                                        rx.foreach(
                                            NewConnectionFormState.type_options,
                                            lambda option: rx.select.item(option["label"], value=option["key"]),
                                        ),
                                    ),
                                    name="type",
                                    on_change=NewConnectionFormState.handle_type_select,
                                    default_value="SID",
                                    width="100%",
                                ),
                                spacing="0",
                            ),
                            # ===  SID or SN  =========================================================
                            rx.match(
                                NewConnectionFormState.connection_def.type,
                                ("SID", rx.vstack(
                                    rx.text.strong(
                                        "SID",
                                        rx.text.span(" *", color=rx.color("red", 9)),
                                    ),
                                    rx.input(
                                        name="sid",
                                        required=True,
                                        on_blur=NewConnectionFormState.handle_validation,
                                    ),
                                    spacing="0",
                                    width="100%",
                                    align="stretch",
                                )),
                                ("SN", rx.vstack(
                                    rx.text.strong(
                                        "Service Name",
                                        rx.text.span(" *", color=rx.color("red", 9)),
                                    ),
                                    rx.input(
                                        name="sn",
                                        required=True,
                                        on_blur=NewConnectionFormState.handle_validation,
                                    ),
                                    spacing="0",
                                    width="100%",
                                    align="stretch",
                                )),
                            ),
                            width="100%",
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button("Cancel", variant="soft", color_scheme="gray"),
                            ),
                            rx.dialog.close(
                                rx.button("Submit", type="submit", disabled=NewConnectionFormState.is_disabled),
                            ),
                            spacing="3",
                            justify="end",
                            width="100%",
                        ),
                        spacing="4",
                    ),
                    on_submit=NewConnectionFormState.handle_submit,
                    reset_on_submit=True,
                    padding_top="20px",
                ),
                max_width="400px",
            ),
            on_open_change=NewConnectionFormState.handle_open_change,
        )

@rx.page("new_connection_form", title="New Connection Form")
def new_connection_form_page() -> rx.Component:
    return rx.center(
        NewConnectionForm().create_v1(),
        width="100%",
        height="50vh",
    )