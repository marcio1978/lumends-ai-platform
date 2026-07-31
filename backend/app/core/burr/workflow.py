"""
LAP Burr Workflow
"""

from burr.core import (
    ApplicationBuilder,
    State,
)

from app.core.burr.actions import (
    receive_message,
    generate_response,
)


def create_workflow(message: str):

    app = (
        ApplicationBuilder()
        .with_state(
            State(
                {
                    "message": message
                }
            )
        )
        .with_actions(
            receive_message,
            generate_response,
        )
        .with_entrypoint(
            "receive_message"
        )
        .with_transitions(
            ("receive_message", "generate_response"),
        )
        .build()
    )

    return app
