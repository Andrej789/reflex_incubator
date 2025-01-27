# 3rd party modules
import reflex as rx


class NewConnectionFormState(rx.State):
    type_selected_key: str = "SID",
    type_options: list[dict[str, str]] = [
        {"key": "SID", "label": "SID"},
        {"key": "SN", "label": "Service Name"},
    ]
    
    @rx.event
    def handle_submit(self, form_dict: dict) -> None:
        pass

    @rx.event
    def handle_type_select(self, value: str) -> None:
        for option in self.type_options:
            if option["key"] == value:
                self.type_selected_key = option["key"]
                break


class NewConnectionForm():

    def create_v1(self) -> rx.Component:
        return rx.card(
            rx.vstack(
                rx.icon(
                    "x", 
                    size=13, 
                    color=rx.color("gray", 7),
                    _hover={"color": f'{rx.color("black")}'}
                ),
                direction="column",
                widtth="100%",
                align="end",
            ),
            rx.form(
                rx.vstack(
                    # ===  Connection name  ===
                    rx.vstack(
                        rx.text.strong(
                            "Connection Name",
                            rx.text.span(" *", color=rx.color("red", 9)),
                        ),
                        rx.input(
                            name="connection_name",
                            required=True,
                        ),
                        spacing="0",
                        width="100%",
                        align="stretch",
                    ),
                    # ===  Separator  ===
                    rx.vstack(
                        rx.divider(
                            width="100%",
                            bg=f'linear-gradient(to right, transparent 0%, {rx.color("gray")} 20%, {rx.color("gray")} 80%, transparent 100%)',
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    # ===  Username  ===
                    rx.vstack(
                        rx.text.strong(
                            "Username",
                            rx.text.span(" *", color=rx.color("red", 9)),
                        ),
                        rx.input(
                            name="username",
                            required=True,
                        ),
                        spacing="0",
                        width="100%",
                        align="stretch",
                    ),
                    # ===  Password  ===
                    rx.vstack(
                        rx.text.strong(
                            "Password",
                            rx.text.span(" *", color=rx.color("red", 9)),
                        ),
                        rx.input(
                            name="password",
                            type="password",
                            required=True,
                        ),
                        spacing="0",
                        width="100%",
                        align="stretch",
                    ),
                    # ===  Host  ===
                    rx.vstack(
                        rx.text.strong(
                            "Hostname",
                            rx.text.span(" *", color=rx.color("red", 9)),
                        ),
                        rx.input(
                            name="hostname",
                            required=True,
                        ),
                        spacing="0",
                        width="100%",
                        align="stretch",
                    ),
                    # ===  Port  ===
                    rx.vstack(
                        rx.text.strong(
                            "Port"
                        ),
                        rx.input(
                            name="port",
                            default_value="1521",
                            required=True,
                        ),
                        spacing="0",
                        width="100%",
                        align="stretch",
                    ),
                    # ===  Type  ===
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
                        # ===  SID or SN  ===
                        rx.match(
                            NewConnectionFormState.type_selected_key,
                            ("SID", rx.vstack(
                                rx.text.strong(
                                    "SID"
                                ),
                                rx.input(
                                    name="sid",
                                    required=True,
                                ),
                                spacing="0",
                                width="100%",
                                align="stretch",
                            )),
                            ("SN", rx.vstack(
                                rx.text.strong(
                                    "Service Name"
                                ),
                                rx.input(
                                    name="sn",
                                    required=True,
                                ),
                                spacing="0",
                                width="100%",
                                align="stretch",
                            )),
                        ),
                        width="100%",
                    ),
                    spacing="4",
                ),
                on_submit=NewConnectionFormState.handle_submit,
                reset_on_submit=True
            ),
            min_width="400px",
        )

@rx.page("new_connection_form", title="New Connection Form")
def new_connection_form_page() -> rx.Component:
    return rx.center(
        NewConnectionForm().create_v1(),
        width="100%",
        height="50vh",
    )