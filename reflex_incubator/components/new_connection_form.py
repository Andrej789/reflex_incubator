# Python modules
from typing import Literal, Optional

# 3rd party modules
import reflex as rx


class NewConnectionFormState(rx.State):
    # Form fields ==============
    connection_name: str
    username: str
    # ==========================
    dialog_action: str # Which button (Submit, Cancel, Open) was selected on the form
    is_dialog_open: bool = False
    type_options: list[dict[str, str]] = [
        {"key": "SID", "label": "SID"},
        {"key": "SN", "label": "Service Name"},
    ]

    @rx.var
    def connection_name_empty(self) -> bool:
        return not self.connection_name.strip()

    @rx.var
    def username_empty(self) -> bool:
        return not self.username.strip()

    def toggle_dialog(self) -> None:
        """ Open or close the dialog."""
        self.is_dialog_open = not self.is_dialog_open
    
    @rx.event
    def handle_open(self) -> None:
        """Called after pressing form trigger button."""
        self.dialog_action = "open"
        self.handle_reset()
        self.toggle_dialog()

    @rx.event
    def handle_submit(self) -> None:
        """Called after pressing the Submit button."""
        self.dialog_action = "submit"
        is_form_valid = self.handle_validation()
        if is_form_valid:
            self.toggle_dialog()
    
    @rx.event
    def handle_cancel(self) -> None:
        """Called after pressing the Cancel button."""
        self.dialog_action = "cancel"
        self.toggle_dialog()
    
    def handle_validation(self) -> bool:
        """Validate all form fields."""
        result = False
        if not self.connection_name_empty and not self.username_empty:
            result = True
        return result

    def handle_reset(self):
        """Reset form fields to default state."""
        self.connection_name = ""
        self.username = ""


class NewConnectionForm():

    def form_field(self, name: str, label: str, placeholder: str = "", type: str = "text", required: bool = False) -> rx.Component:
        return rx.form.field(
            rx.flex(
                rx.form.label(label),
                rx.form.control(
                    rx.input(
                        placeholder=placeholder,
                        type=type,
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="1",
            ),
            name=name,
            width="100%",
        )

    def create_v1(self) -> rx.Component:
        return rx.flex(
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("plus", size=20),
                        rx.text("New Connection"),
                        on_click=NewConnectionFormState.handle_open
                    ),
                ),
                rx.dialog.content(
                    rx.hstack(
                        rx.badge(
                            rx.icon(tag="file-plus", size=48),
                            radius="full",
                            padding="0.65rem",
                        ),
                        rx.vstack(
                            rx.dialog.title(
                                "New Connection", 
                                style={"margin-top": "10px", "margin-bottom": "0px", "padding-bottom": "0px"},
                            ),
                            rx.dialog.description(
                                "Fill the form with connection's metadata", 
                                style={"margin-top": "0px", "padding-top": "0px"},
                            ),
                        ),
                    ),
                    rx.vstack(
                        rx.form.root(
                            rx.flex(
                                # ===  Connection name  ===========================================
                                rx.form.field(
                                    rx.flex(
                                        rx.form.label("Connection Name"),
                                        rx.form.control(
                                            rx.input(
                                                name="connection_name",
                                                placeholder="Enter connection name",
                                                value=NewConnectionFormState.connection_name,
                                                type="text",
                                                required=True,
                                                on_change=NewConnectionFormState.set_connection_name,
                                            ),
                                            as_child=True,
                                        ),
                                        rx.form.message(
                                            "Connection name cannot be empty",
                                            match="valueMissing",
                                            force_match=NewConnectionFormState.connection_name_empty,
                                            color=rx.color("red", 10),
                                        ),
                                        direction="column",
                                        spacing="1",
                                    ),
                                    name="connection_name",
                                    width="100%",
                                    server_invalid=NewConnectionFormState.connection_name_empty,
                                ),
                                # ===  User name  ===========================================------
                                rx.form.field(
                                    rx.flex(
                                        rx.form.label("Username"),
                                        rx.form.control(
                                            rx.input(
                                                name="username",
                                                placeholder="Enter username",
                                                value=NewConnectionFormState.username,
                                                type="text",
                                                required=True,
                                                on_change=NewConnectionFormState.set_username,
                                            ),
                                            as_child=True,
                                        ),
                                        rx.form.message(
                                            "Username cannot be empty",
                                            match="valueMissing",
                                            force_match=NewConnectionFormState.username_empty,
                                            color=rx.color("red", 10),
                                        ),
                                        direction="column",
                                        spacing="1",
                                    ),
                                    name="username",
                                    width="100%",
                                    server_invalid=NewConnectionFormState.username_empty,
                                ),
                                direction="column",
                                style={"margin-bottom": "10px"},
                            ),
                            # ===  Buttons  =======================================================
                            rx.flex(
                                rx.dialog.close(
                                    rx.button(
                                        "Cancel",
                                        on_click=NewConnectionFormState.handle_cancel,
                                        variant="soft",
                                        color_scheme="gray",
                                        min_width="120px",
                                    ),
                                ),
                                rx.dialog.close(
                                    rx.form.submit(
                                        rx.button(
                                            "Submit",
                                            on_click=NewConnectionFormState.handle_submit,
                                            type="submit",
                                            min_width="120px",
                                        ),
                                    ),
                                ),
                                spacing="3",
                                direction="row",
                                justify="end",
                            ),
                            style={"margin-top": "15px"},
                        ),
                    ),
                    max_width="450px",
                ),
                open=NewConnectionFormState.is_dialog_open,
                reset_on_submit=True,
                #on_open_change=NewConnectionFormState.handle_open_change,
            ),
        )

@rx.page("new_connection_form", title="New Connection Form")
def new_connection_form_page() -> rx.Component:
    return rx.center(
        NewConnectionForm().create_v1(),
        height="50vh",
    )