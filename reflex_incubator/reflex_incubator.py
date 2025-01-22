"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


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
