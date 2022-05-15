import random


def get_random_bootstrap_color(request):
    color = random.choice(
        (
            "primary",
            "primary",
            "secondary",
            "success",
            "danger",
            "dark"
        )
    )

    return {'random_bootstrap_color': color}
