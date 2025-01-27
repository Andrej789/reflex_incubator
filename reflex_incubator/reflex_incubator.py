# 3rd party modules
import reflex as rx

# Mine modules
from rxconfig import config
from .components.credit_card import credit_card
from .components.personal_workspace_dashboard import css, blink, dimensions, create_box_dimensions
from .components.menu_v1 import menu_v1
from .components.text_and_label import text_and_label
from .components.validate_email import validate_email
from .components.area_chart_v1 import area_chart_v1
from .components.new_connection_form import new_connection_form_page


class AppState(rx.State):
    """The app state."""
    pass


@rx.page(route="/", title="Index")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.flex(
            rx.heading(
                "Welcome in Reflex Incubator", 
                size="7",
                color=rx.color("accent", 12),
            ),
            width="100%",
            height="97vh",
            justify_content="center",
            align_items="center",
            bg=rx.color("accent"),
        ),
        bg=rx.color("accent", 12),
    )


app = rx.App(
    theme=rx.theme(
        accent_color="grass",
    ),
)
#app.add_page(index)