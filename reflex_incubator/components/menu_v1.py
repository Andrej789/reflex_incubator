# 3rd party modules
import reflex as rx


class Content(rx.State):
    links: list[dict[str, str]] = [
        {"label": "Usage", "link": "#usage", "color": "gray"},
        {"label": "Position and placement", "link": "#position", "color": "gray"},
        {"label": "With other overlays", "link": "#overlays", "color": "gray"},
        {"label": "Manage focus", "link": "#focus", "color": "gray"},
        {"label": "Examples", "link": "#1", "color": "gray"},
        {"label": "Show on focus", "link": "#2", "color": "gray"},
        {"label": "Show on hover", "link": "#3", "color": "gray"},
        {"label": "With form", "link": "#4", "color": "gray"},
    ]

    index: int = 0
    position_y: str = 5 # "10px"

    async def toggle_table_content(self, index: int, item: dict[str, str]) -> None:
        self.links = [
            (
                {**data, "color": rx.color("slate", 11)}
                if data["label"] != item["label"]
                else {**data, "color": rx.color("slate", 12)}
            )
            for data in self.links
        ]
        #self.position_y = f"{10 + (index * 30)}px"
        self.position_y = f"{5 + (index * 30)}px"


def items(index: int, data: dict[str, str]):
    return rx.hstack(
        rx.link(
            rx.text(
                data["label"],
                font_size="12px",
                color=data["color"],
                weight="medium",
                on_click=Content.toggle_table_content(index, data),
            ),
            href=data["link"],
            text_decoration="none",
        ),
        border_left=f"1px solid {rx.color('gray', 5)}",
        width="200px",
        height="30px",
        align="center",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
    )


def item_header():
    return rx.hstack(
        rx.text("Menu Items", font_size="11px", color_scheme="gray", weight="medium"),
        rx.icon(tag="puzzle", size=12),
        width="100%",
        justify="between",
        align="center",
        border_left=f"1px solid {rx.color('gray', 5)}",
        border_radius="0px 5px 5px 0px",
        padding_left="15px",
        padding_right="15px",
        height="30px",
        bg=rx.color("gray", 3),
    )


@rx.page(route="/menu_v1", title="Menu v1")
def menu_v1():
    return rx.center(
        rx.vstack(
            item_header(),
            rx.vstack(
                rx.box(
                    width="3px",
                    height="20px",
                    border_radius="1px",
                    bg=rx.color("blue"),
                    position="absolute",
                    #left="-4.5px",
                    left="1px",
                    top=Content.position_y,
                    transition="all 200ms ease-out",
                ),
                rx.foreach(
                    Content.links,
                    lambda data, index: items(index, data),
                ),
                spacing="0",
                position="relative",
            ),
            spacing="0",
            height="100vh",
            justify="center",
        ),
    )