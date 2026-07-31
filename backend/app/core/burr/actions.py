"""
LAP Burr Actions

Ações executadas pelo workflow Burr.
"""

from burr.core import action


@action(
    reads=["message"],
    writes=["message_received"]
)
def receive_message(state):

    return (
        {},
        state.update(
            message_received=True
        )
    )


@action(
    reads=["message"],
    writes=["response"]
)
def generate_response(state):

    message = state["message"]

    return (
        {},
        state.update(
            response=f"LAP Burr recebeu: {message}"
        )
    )
