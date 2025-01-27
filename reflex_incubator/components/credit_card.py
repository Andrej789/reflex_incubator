# 3rd party modules
import reflex as rx


def main_card() -> rx.Component:
    return rx.container(
        width="100%",
        max_width="500px",
        height="260px",
        z_index="2",
        #margin_left="auto",
        #margin_right="auto",
        position="absolute",
        transform="translate(0px, -200px)",
        box_shadow="0px 30px 60px 0 rgba(90, 116, 148, 0.4)",
        bg="pink",
    )


def card() -> rx.Component:
    """Main card form."""
    return rx.flex( 
        rx.container(
            main_card(),
            # Form settings
            bg="#fff",
            padding="35px",
            max_width="570px",
            width="100%",
            margin="auto",
            border_radius="20px",
            box_shadow="0 30px 60px 0 rgb(90, 116, 148, 0.4)",
        ),
        width="100%",
        height="100vh",
        padding_top="250px",
        padding_bottom="650px",
        direction="column",
    )


@rx.page(route="/credit_card", title="Credit Card")
def credit_card() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(
        # Main card form component
        card(),
        # Page settings
        bg="#ddeefc",
        min_height="100vh",
        display="flex",
        flex_wrap="wrap",
        flex_direction="column",
        align_items="flex-start",
        padding="50px, 15px",
    )
