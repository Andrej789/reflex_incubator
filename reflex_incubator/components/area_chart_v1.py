# Python modules
from dataclasses import dataclass, field
import asyncio

# 3rd party modules
import reflex as rx


@dataclass
class TooltipStyles:
    separator: str = ""
    cursor: bool = False
    wrapper_style: dict = field(
        default_factory=lambda: {"padding": 0, "margin": 0, "width": "150px"},
    )
    view_box: dict = field(
        default_factory=lambda: {"padding": 0, "margin": 0, "width": "150px"},
    )
    item_style: dict = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "fontSize": 11,
            "padding": 0,
            "margin": 0,
            "justify-content": "space-between",
            "display": "flex",
            "textTransform": "capitalize",
            "width": "175px",
        },
    )
    label_style: dict = field(
        default_factory=lambda: {
            "fontSize": 11,
            "padding": 0,
            "fontWeight": "bold",
            "color": rx.color("slate", 12),
        },
    )
    content_style: dict = field(
        default_factory=lambda: {
            "background": rx.color("gray", 2),
            "borderColor": rx.color("gray", 4),
            "borderRadius": "6px",
            "width": "150px",
            "padding": 6,
            "margin": 0,
        },
    )


tooltip_styles = TooltipStyles()


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )

@rx.page(route="/area_chart_v1", title="Area chart v.1")
def area_chart_v1():

    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Area Chart",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.area_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    fill_opacity=0.5,
                    stroke=rx.color("slate", 5),
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill=rx.color("green", 5), #ComponentWrapperState.default_theme[0],
                    stroke=rx.color("green", 7), #ComponentWrapperState.default_theme[3],
                ),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.y_axis(
                    data_key="desktop",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 0},
            ),
            info(
                "Trending up by 5.2% this month",
                "2",
                "January - June 2024",
                "start",
            ),
            width="100%",
            margin_left="20px",
            margin_right="20px",
        ),
        width="100%",
        padding="0.5em",
    )