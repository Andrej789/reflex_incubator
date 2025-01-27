# Python modules
from typing import Any

# 3rd party modules
import reflex as rx


# styles
css: dict = {
    "app": {
        "_dark": {"bg": "#1f2128"},
        "_light": {"bg": "#312e2a"},
        "font_family": "Gill Sans",
    },
    "header": {
        "width": "100%",
        "height": "7vh",
        "box_shadow": "0px, 8px, 16px 0px rgba(0, 0, 0, 0.35)",
        "justify_content": "center",
        "padding": ["0 1rem", "0 1rem", "0 1rem", "0 4rem", "0 10rem"],
        "transition": "all 400ms ease",
        "_dark": {"bg": "#141518"},
        "_light": {"bg": "#292824"},
    },
    "content": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
    },
    "workSpace": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "height": "100vh",
    },
    "main": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "height": "100vh",
    },
}


def create_box_dimensions(width: str, height: str) -> dict[str, Any]:
    return {
        "width": width,
        "height": height,
        "box_shadow": "0px 10px 20px 0px rgba(0, 0, 0, 0.5)",
        "_hover": {"box_shadow": "none"},
        "transition": "all 450ms ease",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
    }


dimensions: dict[str, dict[str, Any]] = {
    "square": create_box_dimensions("5em", "5em"),
    "rectangle": create_box_dimensions("5em", "10.5em"),
    "custom_1": create_box_dimensions("10.5em", "10.5em"),
    "custom_2": create_box_dimensions("10.5em", "5em"),
}


# Blinking animation for display cursor
blink: dict = {
    "@keyframes blink": {
        "0%": {"opacity": "0"},
        "50%": {"opacity": "1"},
        "100%": {"opacity": "0"},
    },
    "animation": "blink 0.9s infinite",
}


@rx.page(route="/pwd", title="Personal Workspace Dashboard")
def personal_workspace_dashboard() -> rx.Component:
    return rx.container()